import asyncio
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.scraper.doc_scraper import DocScraper
from src.utils.cleaner import Cleaner
from src.utils.logger import logger

async def test_pipeline():
    TEST_URL = "https://wiza.co/api-docs" 
    
    logger.info(f"🧪 STARTING CRAWLER TEST ON: {TEST_URL}")
    
    async with DocScraper() as scraper:
        # 1. Navigate
        success = await scraper.navigate_to_url(TEST_URL)
        if not success:
            logger.error("❌ Navigation failed")
            return

        # 2. CRAWL (The new magic step)
        # This will click sidebar links and gather EVERYTHING
        raw_markdown = await scraper.crawl_full_documentation()
        
        # 3. Clean
        cleaned_text = Cleaner.clean_markdown(raw_markdown)
        
        # 4. Stats
        tokens = Cleaner.count_tokens(cleaned_text)
        logger.info(f"📦 Total Content Size: {len(cleaned_text)} chars")
        logger.info(f"🪙 Estimated Tokens: {tokens}")
        
        if tokens > 0:
            logger.success("✅ CRAWL PASSED: Retrieved comprehensive API data.")
            # Print a snippet from the MIDDLE to prove we got deep content
            mid_point = len(cleaned_text) // 2
            print("\n--- RANDOM SNIPPET FROM MIDDLE ---")
            print(cleaned_text[mid_point : mid_point+500])
            print("----------------------------------\n")
        else:
            logger.error("❌ CRAWL FAILED: No content.")

if __name__ == "__main__":
    asyncio.run(test_pipeline())