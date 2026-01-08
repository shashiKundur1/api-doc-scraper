import asyncio
import trafilatura
from playwright.async_api import async_playwright, Playwright, Browser, BrowserContext, Page, Route, Error as PlaywrightError
from config.settings import settings
from src.utils.logger import logger

class DocScraper:
    """
    Async Playwright Scraper optimized for API documentation.
    Implements 2025 best practices: Context isolation, Async I/O, Stealth, Resource Blocking, Auto-Waiting, and Smart Extraction.
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
            logger.info(f"Browser launched successfully (Headless: {settings.HEADLESS})")
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

        max_retries = 3
        for attempt in range(max_retries):
            try:
                logger.info(f"Navigating to {url} (Attempt {attempt + 1})")
                response = await self.page.goto(
                    url, 
                    wait_until="domcontentloaded", 
                    timeout=settings.TIMEOUT
                )

                if not response or response.status >= 400:
                    logger.error(f"HTTP Error {response.status if response else 'No Response'}")
                    return False
                
                await self.ensure_content_loaded()
                logger.success(f"Successfully loaded and hydrated {url}")
                return True

            except PlaywrightError as e:
                logger.warning(f"Navigation issue: {e}. Retrying...")
                await asyncio.sleep(2)
        
        return False

    async def ensure_content_loaded(self):
        """Ensures page content is fully hydrated and stable."""
        try:
            logger.info("Waiting for content hydration...")
            await self.page.locator("h1, h2, article, main, [role='main']").first.wait_for(
                state="visible", timeout=10000
            )
            
            # Smart Scroll to trigger lazy loading
            await self._smart_scroll()

        except Exception as e:
            logger.warning(f"Hydration check warning: {e}")

    async def _smart_scroll(self):
        """
        Scrolls the page to trigger lazy-loading elements.
        Stops when height stabilizes.
        """
        logger.info("Performing smart scroll to load lazy content...")
        last_height = 0
        for _ in range(20): # Max 20 scrolls
            try:
                # Scroll to bottom
                await self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                await asyncio.sleep(1) # Wait for network
                
                new_height = await self.page.evaluate("document.body.scrollHeight")
                if new_height == last_height:
                    break # Reached bottom
                last_height = new_height
            except:
                break

    async def extract_content(self) -> str:
        """
        Extracts and cleans content using Trafilatura.
        Returns: Markdown string optimized for LLM processing.
        """
        logger.info("Extracting and cleaning content...")
        
        # 1. Get the full rendered HTML from Playwright
        html = await self.page.content()
        
        # 2. Use Trafilatura to extract main content and convert to Markdown
        extracted_text = trafilatura.extract(
            html,
            output_format='markdown',
            include_comments=False,
            include_tables=True,
            include_links=False, # Reduce token usage
            favor_precision=True
        )

        if not extracted_text:
            logger.warning("Trafilatura failed to extract content. Falling back to raw text.")
            return await self.page.inner_text("body")
            
        logger.success(f"Content extracted successfully ({len(extracted_text)} chars).")
        return extracted_text

    async def close(self):
        logger.info("Closing Playwright resources...")
        if self.context:
            await self.context.close()
        if self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()
        logger.info("Resources closed.")