import asyncio
import json
import os
from playwright.async_api import async_playwright
from src.parser.soup_parser import SoupParser
from src.utils.logger import logger

async def main():
    url = "https://api.contactout.com/"
    logger.info(f"🥣 Starting Soup Scraper on {url}")

    # 1. Fetch Rendered HTML (Playwright)
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url, wait_until="networkidle")
        await page.wait_for_timeout(3000) # Ensure JS renders
        
        # Get the full HTML content
        html_content = await page.content()
        await browser.close()

    # 2. Parse with BeautifulSoup
    logger.info("Parsing HTML structure...")
    parser = SoupParser()
    data = parser.parse_html(html_content)

    # 3. Generate Markdown Output
    md_lines = ["# API Documentation\n"]
    
    for item in data:
        md_lines.append(f"## {item['heading']}\n")
        if item['description']:
            md_lines.append(f"{item['description']}\n")
        
        if item['params']:
            md_lines.append("### Parameters")
            md_lines.append("| Name | Type | Description |")
            md_lines.append("|------|------|-------------|")
            for param in item['params']:
                md_lines.append(f"| {param['name']} | {param['type']} | {param['description']} |")
            md_lines.append("\n")

        if item['code_samples']:
            md_lines.append("### Code Samples")
            for code in item['code_samples']:
                md_lines.append(f"**{code['language']}**")
                md_lines.append(f"```\n{code['code']}\n```\n")
        
        md_lines.append("---\n")

    # 4. Save
    os.makedirs("output", exist_ok=True)
    
    # Save JSON
    with open("output/soup_data.json", "w") as f:
        json.dump(data, f, indent=2)

    # Save Markdown
    with open("output/contactout_docs.md", "w") as f:
        f.write("\n".join(md_lines))

    logger.success(f"🎉 Extracted {len(data)} endpoints using BeautifulSoup!")
    logger.success("Saved to: output/contactout_docs.md")

if __name__ == "__main__":
    asyncio.run(main())