import os
import json
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from src.parser.openapi_parser import OpenApiParser
from src.parser.markdown_generator import MarkdownGenerator

console = Console()

def main():
    # The URL we found in the traffic sniff
    SPEC_URL = "https://wiza.co/api/api-docs/v1/openapi.yaml"

    console.print(Panel.fit(f"[bold blue]🚀 Starting Direct OpenAPI Parsing[/bold blue]\n[yellow]{SPEC_URL}[/yellow]"))

    # 1. Parse
    parser = OpenApiParser(SPEC_URL)
    data = parser.parse()

    # 2. Save Output
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs("output", exist_ok=True)

    # Save JSON
    json_filename = f"output/wiza_openapi_{timestamp}.json"
    with open(json_filename, "w", encoding="utf-8") as f:
        f.write(data.model_dump_json(indent=2))

    # Save Markdown
    md_filename = f"output/wiza_openapi_{timestamp}.md"
    markdown_content = MarkdownGenerator.generate_markdown(data)
    MarkdownGenerator.save_markdown(markdown_content, md_filename)

    console.print(Panel.fit(f"[bold green]✅ Parsing Complete![/bold green]\n"
                            f"Total Endpoints: {len(data.endpoints)}\n"
                            f"JSON: [underline]{json_filename}[/underline]\n"
                            f"Markdown: [underline]{md_filename}[/underline]"))

if __name__ == "__main__":
    main()