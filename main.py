import asyncio
import os
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

# Import all our modules
from src.scraper.doc_scraper import DocScraper
from src.parser.openapi_parser import OpenApiParser
from src.parser.markdown_generator import MarkdownGenerator
from src.ai.gpt_processor import GptProcessor, DocumentationData
from src.utils.cleaner import Cleaner
from src.utils.logger import logger

console = Console()

async def find_spec_url(target_url: str):
    """
    Traffic sniffer to find hidden OpenAPI specs (json/yaml).
    """
    from playwright.async_api import async_playwright
    
    logger.info(f"🕵️‍♀️ Sniffing for OpenAPI Spec on: {target_url}")
    found_spec = None

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        # Listener
        def handle_request(req):
            nonlocal found_spec
            u = req.url.lower()
            if any(ext in u for ext in [".json", ".yaml", ".yml"]) and \
               any(k in u for k in ["swagger", "openapi", "api-docs", "spec"]) and \
               "package.json" not in u:
                found_spec = req.url

        page.on("request", handle_request)
        
        try:
            await page.goto(target_url, wait_until="networkidle", timeout=15000)
            await page.wait_for_timeout(3000)
        except:
            pass
        
        await browser.close()
    
    return found_spec

async def main():
    # 1. Get User Input
    target_url = Prompt.ask("[bold yellow]Enter API Documentation URL[/bold yellow]", default="https://wiza.co/api-docs")
    
    console.print(Panel.fit(f"[bold blue]🚀 Starting Universal API Scraper[/bold blue]\nTarget: {target_url}"))
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    final_data = None
    source_type = "UNKNOWN"

    # --- STRATEGY A: THE "GOLDEN PATH" (OpenAPI Spec) ---
    spec_url = await find_spec_url(target_url)
    
    if spec_url:
        console.print(f"[bold green]✅ JACKPOT! Found OpenAPI Spec:[/bold green] {spec_url}")
        if Prompt.ask("Do you want to use this spec?", choices=["y", "n"], default="y") == "y":
            parser = OpenApiParser(spec_url)
            final_data = parser.parse()
            source_type = "OPENAPI_SPEC"

    # --- STRATEGY B: THE "NUCLEAR OPTION" (AI Crawler) ---
    if not final_data:
        console.print("[bold yellow]⚠️ No spec found or skipped. Switching to AI Visual Crawler...[/bold yellow]")
        
        gpt = GptProcessor()
        master_endpoints = []
        
        async with DocScraper() as scraper:
            if await scraper.navigate_to_url(target_url):
                # Iterate pages
                async for page_data in scraper.get_all_documentation_pages():
                    section = page_data.get("section", "Unknown")
                    content = page_data.get("content", "")
                    
                    if len(content) < 50: continue

                    cleaned = Cleaner.clean_markdown(content)
                    
                    # AI Process
                    try:
                        result = await gpt.process_content(cleaned)
                        if result and result.endpoints:
                            master_endpoints.extend(result.endpoints)
                            logger.success(f"✅ Extracted {len(result.endpoints)} endpoints from '{section}'")
                    except Exception as e:
                        logger.error(f"AI Error: {e}")
        
        if master_endpoints:
            final_data = DocumentationData(endpoints=master_endpoints)
            source_type = "AI_CRAWLER"

    # --- SAVE RESULTS ---
    if final_data and final_data.endpoints:
        os.makedirs("output", exist_ok=True)
        
        # Save JSON
        json_file = f"output/api_{timestamp}.json"
        with open(json_file, "w") as f:
            f.write(final_data.model_dump_json(indent=2))
            
        # Save Markdown
        md_file = f"output/api_{timestamp}.md"
        md_content = MarkdownGenerator.generate_markdown(final_data)
        MarkdownGenerator.save_markdown(md_content, md_file)
        
        console.print(Panel.fit(
            f"[bold green]🎉 Extraction Complete ({source_type})[/bold green]\n"
            f"Endpoints: {len(final_data.endpoints)}\n"
            f"Files: {json_file}, {md_file}"
        ))
    else:
        console.print("[bold red]❌ Failed to extract any data.[/bold red]")

if __name__ == "__main__":
    asyncio.run(main())