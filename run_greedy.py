import asyncio
import json
import os
from playwright.async_api import async_playwright
from src.parser.greedy_soup_parser import GreedySoupParser
from src.utils.logger import logger
from rich.console import Console

console = Console()

async def main():
    url = "https://api.contactout.com/"
    
    # 1. Fetch RAW HTML (Playwright)
    async with async_playwright() as p:
        console.print(f"[bold blue]🚀 Fetching Raw HTML from {url}...[/bold blue]")
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url, wait_until="networkidle")
        await page.wait_for_timeout(5000) # Wait extra time for full load
        html = await page.content()
        await browser.close()

    # 2. Parse Greedily
    console.print("[bold yellow]🥣 Parsing (Greedy Mode)...[/bold yellow]")
    parser = GreedySoupParser()
    data = parser.parse_html(html)

    # 3. Save HUGE Detailed JSON
    os.makedirs("output", exist_ok=True)
    with open("output/contactout_greedy_full.json", "w") as f:
        json.dump(data, f, indent=2)

    # 4. Generate Detailed Markdown
    md_lines = ["# ContactOut API (Full Dump)\n"]
    total_code_blocks = 0
    
    for section in data:
        md_lines.append(f"## {section['heading']}\n")
        md_lines.append(section['description'][:500] + "...\n") # Truncate desc for readability in preview
        
        # Add Code Blocks
        if section['code_samples']:
            md_lines.append("### 💻 Code Examples")
            for i, code in enumerate(section['code_samples']):
                md_lines.append(f"**Block {i+1} ({code['language']})**")
                md_lines.append(f"```\n{code['code']}\n```\n")
                total_code_blocks += 1
        
        md_lines.append("---\n")

    with open("output/contactout_greedy_full.md", "w") as f:
        f.write("\n".join(md_lines))

    console.print(f"[bold green]✅ Extraction Complete![/bold green]")
    console.print(f"📄 Total Sections: {len(data)}")
    console.print(f"💻 Total Code Blocks: {total_code_blocks} (Should match your 55!)")
    console.print("Saved to: [underline]output/contactout_greedy_full.json[/underline]")

if __name__ == "__main__":
    asyncio.run(main())