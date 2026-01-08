import asyncio
import json
import os
from src.scraper.smart_scraper import SmartScraper
from src.utils.logger import logger

async def main():
    scraper = SmartScraper()
    # ContactOut API Docs
    url = "https://api.contactout.com/"
    
    data = await scraper.scrape(url)
    
    if data:
        os.makedirs("output", exist_ok=True)
        with open("output/raw_scrape_data.json", "w") as f:
            json.dump(data, f, indent=2)
        logger.success(f"🎉 Scraped {len(data)} sections. Saved to output/raw_scrape_data.json")
    else:
        logger.error("❌ Scraping failed.")

if __name__ == "__main__":
    asyncio.run(main())