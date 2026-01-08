import json
import os
from rich.console import Console

console = Console()

def convert_to_markdown():
    input_path = "output/raw_scrape_data.json"
    output_path = "output/contactout_raw.md"

    if not os.path.exists(input_path):
        console.print(f"[bold red]❌ File not found: {input_path}[/bold red]")
        return

    console.print(f"[bold blue]📖 Reading {input_path}...[/bold blue]")
    
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    markdown_lines = []
    markdown_lines.append(f"# API Documentation (Raw Export)\n")
    markdown_lines.append(f"**Total Sections:** {len(data)}\n")
    markdown_lines.append("---\n")

    total_code_blocks = 0

    for item in data:
        section_title = item.get("section", "Untitled")
        raw_text = item.get("raw_text", "No text content.")
        code_samples = item.get("code_samples", [])

        # 1. Section Header
        markdown_lines.append(f"## {section_title}\n")

        # 2. Main Text Content
        # We clean up excessive newlines for better readability, but keep the text raw
        cleaned_text = raw_text.replace("\n\n\n", "\n\n")
        markdown_lines.append(f"{cleaned_text}\n")

        # 3. Code Samples (Dumping ALL of them as requested)
        if code_samples:
            markdown_lines.append(f"### Code Samples ({len(code_samples)})\n")
            
            for i, code in enumerate(code_samples):
                # Handle if code is string or dict (depending on which scraper version you ran)
                content = ""
                lang = "text"
                
                if isinstance(code, dict):
                    content = code.get("code", "") or code.get("raw_html", "")
                    lang = code.get("language", "text")
                else:
                    content = str(code)
                    # Simple heuristic detection for language in raw string
                    if "curl" in content.lower(): lang = "bash"
                    elif "{" in content and "}" in content: lang = "json"
                
                markdown_lines.append(f"**Block {i+1}**")
                markdown_lines.append(f"```{lang}\n{content}\n```\n")
                total_code_blocks += 1

        markdown_lines.append("---\n")

    # Save File
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(markdown_lines))

    console.print(f"[bold green]✅ Conversion Complete![/bold green]")
    console.print(f"📄 Output: [underline]{output_path}[/underline]")
    console.print(f"📊 Stats: {len(data)} sections, {total_code_blocks} code blocks written.")

if __name__ == "__main__":
    convert_to_markdown()