import asyncio
import trafilatura
from playwright.async_api import async_playwright, Playwright, Browser, BrowserContext, Page, Route
from config.settings import settings
from src.utils.logger import logger

class DocScraper:
    """
    Async Playwright Scraper & Crawler with Visual Sidebar Detection.
    """
    
    BLOCKED_RESOURCE_TYPES = {
        "image", "stylesheet", "font", "media", "beacon", 
        "csp_report", "imageset", "object", "texttrack"
    }

    BLOCKED_DOMAINS = [
        "google-analytics", "doubleclick", "facebook", "hotjar", "adservice"
    ]

    def __init__(self):
        self.playwright: Playwright = None
        self.browser: Browser = None
        self.context: BrowserContext = None
        self.page: Page = None
        self.user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

    async def __aenter__(self):
        await self.start()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    async def start(self):
        try:
            logger.info("Initializing Playwright Engine...")
            self.playwright = await async_playwright().start()
            self.browser = await self.playwright.chromium.launch(
                headless=settings.HEADLESS,
                args=["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage"]
            )
        except Exception as e:
            logger.error(f"Failed to start Playwright: {e}")
            raise

    async def _handle_route(self, route: Route):
        request = route.request
        if request.resource_type in self.BLOCKED_RESOURCE_TYPES:
            await route.abort()
            return
        if any(domain in request.url for domain in self.BLOCKED_DOMAINS):
            await route.abort()
            return
        await route.continue_()

    async def create_context(self):
        if not self.browser:
            await self.start()

        self.context = await self.browser.new_context(
            user_agent=self.user_agent,
            viewport={"width": 1920, "height": 1080},
            device_scale_factor=1,
            locale="en-US"
        )
        await self.context.route("**/*", self._handle_route)
        self.page = await self.context.new_page()
        self.page.set_default_timeout(settings.TIMEOUT)

    async def navigate_to_url(self, url: str) -> bool:
        if not self.page:
            await self.create_context()
        try:
            logger.info(f"Navigating to {url}")
            response = await self.page.goto(url, wait_until="domcontentloaded", timeout=settings.TIMEOUT)
            if not response or response.status >= 400:
                logger.error(f"HTTP Error {response.status if response else 'No Response'}")
                return False
            await self.ensure_content_loaded()
            return True
        except Exception as e:
            logger.error(f"Navigation failed: {e}")
            return False

    async def ensure_content_loaded(self):
        try:
            # Wait for any heading to ensure render
            await self.page.locator("h1, h2, h3").first.wait_for(state="visible", timeout=5000)
        except:
            pass

    async def extract_content(self) -> str:
        html = await self.page.content()
        return trafilatura.extract(html, output_format='markdown', include_comments=False) or ""

    async def get_all_documentation_pages(self):
        """
        Iterates through sidebar links using VISUAL POSITION detection.
        This ignores class names and looks for links on the left side of the screen.
        """
        logger.info("🕷️ Scanning for sidebar using Visual Position (Nuclear Option)...")
        
        # 1. Get ALL links on the page
        all_links = await self.page.locator("a").all()
        sidebar_candidates = []
        
        logger.info(f"Analyzing {len(all_links)} visible links...")
        
        for link in all_links:
            try:
                # Get visual bounding box
                box = await link.bounding_box()
                if not box: continue
                
                # VISUAL LOGIC: Sidebar is usually on the left (x < 350px)
                # and usually below the top header (y > 50px)
                if (box['x'] < 350 and 
                    box['y'] > 50 and 
                    box['width'] > 0 and 
                    box['height'] > 0):
                    
                    text = await link.inner_text()
                    text = text.strip()
                    
                    # Filter empty or irrelevant links
                    if text and len(text) > 2 and text.lower() not in ["home", "logo", "back", "top", "sign in", "login"]:
                         sidebar_candidates.append({"text": text, "locator": link, "y": box['y']})
            except:
                continue

        if not sidebar_candidates:
            logger.error("❌ Visual detection failed. Returning current page only.")
            yield {"url": self.page.url, "content": await self.extract_content()}
            return

        # Sort by Y position (Top to Bottom) to crawl in order
        sidebar_candidates.sort(key=lambda item: item['y'])
        
        logger.success(f"✅ Found {len(sidebar_candidates)} visual sidebar links.")
        
        seen_texts = set()
        count = 0
        
        # Limit to 20 sections to prevent infinite runs in testing
        for item in sidebar_candidates:
            if count >= 20: break
            
            text = item["text"]
            if text in seen_texts: continue
            seen_texts.add(text)
            
            try:
                logger.info(f"➡️ Visiting: {text}")
                
                # Scroll & Click
                await item["locator"].scroll_into_view_if_needed()
                await item["locator"].click(force=True)
                
                # Wait for SPA Hydration
                await asyncio.sleep(1.0)
                
                content = await self.extract_content()
                if content:
                    yield {"section": text, "content": content}
                    count += 1
            except Exception as e:
                logger.warning(f"Failed to visit {text}: {e}")

    async def close(self):
        logger.info("Closing Playwright resources...")
        if self.context:
            await self.context.close()
        if self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()