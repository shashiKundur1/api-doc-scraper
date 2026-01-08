import asyncio
import json
import os
from src.ai.gpt_processor import GptProcessor, DocumentationData
from src.parser.markdown_generator import MarkdownGenerator
from src.utils.logger import logger
from rich.console import Console
from rich.panel import Panel

console = Console()

async def process_data():
    console.print(Panel.fit("[bold blue]🧠 Starting NLP Post-Processing[/bold blue]"))

    # 1. Load Data
    with open("output/raw_scrape_data.json", "r") as f:
        data = json.load(f)

    # 2. Strategy Selection
    # If duplicate data detected, we only process the FIRST entry (which is the full page)
    # and ask AI to split it.
    is_duplicate = len(data) > 1 and data[0]['raw_text'] == data[1]['raw_text']
    
    if is_duplicate:
        logger.warning("⚠️ Duplicate content detected. Switching to 'Single-Pass Full Extraction'.")
        items_to_process = [data[0]] # Just take the first one (full page)
    else:
        logger.info("✅ Unique sections detected. Processing individually.")
        items_to_process = data

    gpt = GptProcessor(model="gpt-4o") # Force High Intelligence
    master_endpoints = []

    # 3. AI Processing Loop
    for item in items_to_process:
        section_name = item['section']
        raw_text = item['raw_text']
        code_samples = item.get('code_samples', [])
        
        # Construct a Context-Rich Prompt
        # We explicitly inject the code samples so the AI doesn't miss them
        context_text = f"""
        SECTION: {section_name}
        
        --- MAIN TEXT CONTENT ---
        {raw_text}
        
        --- EXTRACTED CODE SNIPPETS (CRITICAL) ---
        The following code blocks were found in this section. Match them to their endpoints:
        {json.dumps(code_samples, indent=2)}
        """

        try:
            result = await gpt.process_content(context_text)
            if result and result.endpoints:
                master_endpoints.extend(result.endpoints)
                logger.success(f"✅ Extracted {len(result.endpoints)} endpoints from '{section_name}'")
        except Exception as e:
            logger.error(f"Failed to process '{section_name}': {e}")

    # 4. Generate Markdown
    if master_endpoints:
        final_data = DocumentationData(endpoints=master_endpoints)
        
        # Save JSON
        with open("output/final_clean_api.json", "w") as f:
            f.write(final_data.model_dump_json(indent=2))
            
        # Save Markdown
        md_content = MarkdownGenerator.generate_markdown(final_data)
        MarkdownGenerator.save_markdown(md_content, "output/final_clean_api.md")
        
        console.print(Panel.fit(f"[bold green]✨ Processing Complete![/bold green]\nSaved to: output/final_clean_api.md"))
    else:
        logger.error("❌ No endpoints extracted.")

if __name__ == "__main__":
    asyncio.run(process_data())