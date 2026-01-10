import asyncio
from playwright.async_api import async_playwright
from src.utils.logger import logger
from urllib.parse import urljoin, urlparse

class SmartScraper:
    async def scrape(self, base_url: str):
        """
        Robust Scraper: Collects URLs (including anchors) and visits them.
        """
        async with async_playwright() as p:
            # 1. Setup
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(viewport={"width": 1600, "height": 1200}) 
            page = await context.new_page()
            
            logger.info(f"🚀 Initializing: {base_url}...")
            
            # Extract domain for lenient filtering
            parsed_base = urlparse(base_url)
            base_domain = parsed_base.netloc.replace("www.", "")
            
            try:
                await page.goto(base_url, wait_until="domcontentloaded", timeout=60000)
                await page.wait_for_timeout(3000) 
            except Exception as e:
                logger.error(f"   ❌ Initial navigation failed: {e}")
                await browser.close()
                return []

            # --- PHASE 1: COLLECT URLs ---
            logger.info("🕵️‍♀️ Phase 1: Collecting Navigation Links...")
            
            sidebar_selectors = [
                "nav a", "aside a", "#toc a", ".navigation a", 
                "div[class*='sidebar'] a", "div[class*='menu'] a",
                "ul a", "li a"
            ]
            
            found_links = []
            
            # 1. Find Sidebar
            for sel in sidebar_selectors:
                elements = await page.locator(sel).all()
                if len(elements) > 5:
                    logger.success(f"   ✅ Found sidebar using: '{sel}' ({len(elements)} items)")
                    found_links = elements
                    break
            
            # 2. Fallback
            if len(found_links) < 5:
                logger.warning("   ⚠️ Sidebar weak. Switching to GREEDY search.")
                found_links = await page.locator("a").all()

            # 3. Process Links
            urls_to_visit = []
            seen_urls = set()
            
            logger.info("   🔍 filtering links...")
            
            for link in found_links:
                try:
                    href = await link.get_attribute("href")
                    text = await link.inner_text()
                    
                    if not href or not text: continue
                    
                    text = text.strip()
                    # FIX: Allow hash links for Single Page Apps (SPA)
                    if href.startswith(("#", "/")):
                        full_url = urljoin(base_url, href)
                    else:
                        full_url = href

                    # --- FILTERS ---
                    if len(text) < 2: continue 
                    if full_url in seen_urls: continue
                    # FIX: removed '#' from ignored prefixes
                    if href.startswith(("javascript", "mailto", "tel")): continue
                    
                    # Domain Check
                    if base_domain not in full_url:
                        # logger.warning(f"      Skipping external link: {text} -> {full_url}")
                        continue
                    
                    seen_urls.add(full_url)
                    urls_to_visit.append({"url": full_url, "title": text})
                except: pass

            logger.info(f"   📊 Collected {len(urls_to_visit)} unique pages/sections to scrape.")

            # --- PHASE 2: VISIT & SCRAPE ---
            results = []
            content_selector = "#content-area" 

            for i, item in enumerate(urls_to_visit): 
                url = item["url"]
                title = item["title"]
                
                try:
                    logger.info(f"[{i+1}/{len(urls_to_visit)}] 🚀 Visiting: {title}")
                    
                    try:
                        # Handle hash navigation vs full page load
                        if "#" in url and url.split("#")[0] == page.url.split("#")[0]:
                            # Just click if it's on the same page (faster/safer for SPA)
                            # Try to find the link again to click it
                            await page.goto(url, wait_until="domcontentloaded")
                        else:
                            await page.goto(url, wait_until="domcontentloaded", timeout=20000)
                        
                        await page.wait_for_timeout(1000) 
                    except:
                        continue

                    # 1. Find Content
                    content_area = page.locator(content_selector).first
                    if not await content_area.is_visible():
                        content_area = page.locator("main").first
                    if not await content_area.is_visible():
                        content_area = page.locator("body").first

                    # 2. Click Interactive Elements
                    await self._click_interactive_elements(content_area, page)

                    # 3. Extract Code
                    code_blocks = await self._extract_code_via_copy_buttons(content_area)
                    
                    # 4. Extract Text
                    full_text = await content_area.inner_text()

                    results.append({
                        "section": title,
                        "raw_text": full_text,
                        "code_samples": code_blocks 
                    })
                    
                    logger.success(f"      ✅ Captured {len(code_blocks)} code snippets")

                except Exception as e:
                    logger.error(f"      ❌ Failed to process {title}: {e}")

            await browser.close()
            return results

    async def _click_interactive_elements(self, content_area, page):
        keywords = ["200", "201", "400", "401", "403", "404", "500", "cURL", "JSON", "Response", "Request", "Body"]
        for word in keywords:
            try:
                candidates = await content_area.locator(f"text={word}").all()
                for el in candidates:
                    if await el.is_visible():
                        txt = await el.inner_text()
                        if len(txt) < 15: 
                            await el.click(force=True, timeout=500)
                            await page.wait_for_timeout(100)
            except: pass

    async def _extract_code_via_copy_buttons(self, content_area):
        collected_code = []
        unique_codes = set()

        copy_buttons = await content_area.locator("text=Copy").all()
        if not copy_buttons:
            copy_buttons = await content_area.locator("button[aria-label*='copy' i]").all()

        for btn in copy_buttons:
            try:
                if not await btn.is_visible(): continue
                
                btn_handle = await btn.element_handle()
                
                code_text = await btn_handle.evaluate("""(btn) => {
                    let sibling = btn.nextElementSibling;
                    while(sibling) {
                        if (sibling.tagName === 'PRE') return sibling.innerText;
                        sibling = sibling.nextElementSibling;
                    }
                    let parent = btn.parentElement;
                    let depth = 0;
                    while(parent && depth < 4) {
                        let pre = parent.querySelector('pre');
                        if (pre) return pre.innerText;
                        parent = parent.parentElement;
                        depth++;
                    }
                    return null;
                }""")

                if code_text and len(code_text) > 5 and code_text not in unique_codes:
                    unique_codes.add(code_text)
                    lang = "bash" if "curl" in code_text.lower() else "json" if "{" in code_text else "text"
                    collected_code.append({"language": lang, "code": code_text})
            except: pass

        # Fallback
        pres = await content_area.locator("pre").all()
        for pre in pres:
            try:
                text = await pre.inner_text()
                if text and text not in unique_codes:
                    unique_codes.add(text)
                    collected_code.append({"language": "default", "code": text})
            except: pass

        return collected_code