import asyncio
import os
import json
from src.scraper.smart_scraper import SmartScraper
from src.parser.markdown_generator import MarkdownGenerator
from src.utils.logger import logger

# Output paths
JSON_OUTPUT = "output/raw_scrape.json"
MARKDOWN_OUTPUT = "output/final_documentation.md"

async def main():
    logger.info("🚀 Starting Smart Doc Scraper...")
    
    url = input("🌐 Enter URL: ").strip()
    if not url: return

    # 1. Scrape
    scraper = SmartScraper()
    processed_data = await scraper.scrape(url)

    if not processed_data:
        logger.error("❌ No data captured.")
        return

    # 2. SAVE JSON (This was missing!)
    # We must save the data to disk so publish_to_notion.py can read it
    os.makedirs("output", exist_ok=True)
    with open(JSON_OUTPUT, "w", encoding="utf-8") as f:
        json.dump(processed_data, f, indent=4, ensure_ascii=False)
    logger.success(f"💾 Saved raw data to: {JSON_OUTPUT}")

    # 3. Generate Markdown
    MarkdownGenerator.generate_doc(processed_data, MARKDOWN_OUTPUT)
    
    logger.info(f"\n🎉 Done! You can now run: python publish_to_notion.py")

if __name__ == "__main__":
    asyncio.run(main())