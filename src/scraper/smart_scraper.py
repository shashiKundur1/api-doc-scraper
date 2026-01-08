import asyncio
from playwright.async_api import async_playwright
from src.utils.logger import logger
from src.ai.selector_agent import SelectorAgent

class SmartScraper:
    async def scrape(self, url: str):
        async with async_playwright() as p:
            # 1. Launch & Navigate
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            logger.info(f"🚀 Navigating to {url}...")
            await page.goto(url, wait_until="domcontentloaded")
            await page.wait_for_timeout(3000) # Wait for render

            # 2. Get Selectors (AI + Fallback)
            # We skip the AI step for now to ensure we use the KNOWN GOOD selectors from your debug
            # In a real universal app, we'd keep the AI, but for this specific request, we hardcode reliability.
            
            selectors = {
                "sidebar": "#toc .toc-link",  # Proven by logs
                "content": ".content",        # Proven by logs
                "code": "pre.highlight",      # Proven by logs
                "params": "table, ul, .parameters" # General best guess
            }
            
            logger.info(f"Using Proven Selectors: {selectors}")

            # 3. Scrape
            # A. Get all Sidebar Links
            links = await page.locator(selectors["sidebar"]).all()
            logger.info(f"Found {len(links)} navigation items.")

            results = []
            
            # Iterate through unique links (deduplicate by text)
            seen_sections = set()
            
            # Limit to first 10 for testing speed, remove [:10] for full run
            for i, link in enumerate(links): 
                try:
                    text = await link.inner_text()
                    section_name = text.strip()
                    
                    if not section_name or section_name in seen_sections: continue
                    seen_sections.add(section_name)
                    
                    logger.info(f"➡️ Visiting: {section_name}")
                    
                    # Force click to handle overlays
                    await link.click(force=True)
                    await page.wait_for_timeout(1000) # Fast wait for hydration

                    # B. Extract Content
                    # Scoping to .content ensures we don't grab the sidebar text by accident
                    content_area = page.locator(selectors["content"])
                    
                    # 1. Capture Code Blocks (The critical part)
                    code_blocks = []
                    # Try specific 'pre.highlight' first (Slate theme standard)
                    pres = await content_area.locator(selectors["code"]).all()
                    for pre in pres:
                        code_text = await pre.inner_text()
                        if code_text and len(code_text) > 10:
                            code_blocks.append(code_text)
                    
                    # 2. Capture Text Content (for the AI to process later)
                    full_text = await content_area.inner_text()
                    
                    # Store result
                    results.append({
                        "section": section_name,
                        "raw_text": full_text,     # Main description + params
                        "code_samples": code_blocks # Explicit code snippets
                    })
                    
                    logger.success(f"   ✅ Extracted {len(code_blocks)} code blocks from {section_name}")

                except Exception as e:
                    logger.warning(f"   ⚠️ Failed section: {e}")

            await browser.close()
            return results