import asyncio
import json
import os
from dotenv import load_dotenv
from notion_client import AsyncClient
from src.utils.logger import logger

# 1. Load Config
load_dotenv()
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
PAGE_ID = os.getenv("NOTION_PAGE_ID")
INPUT_FILE = "output/raw_scrape.json"

def chunk_text(text: str, max_len: int = 2000) -> list[str]:
    """Splits text into chunks of max_len to satisfy Notion's API limits."""
    if not text:
        return []
    return [text[i:i+max_len] for i in range(0, len(text), max_len)]

def normalize_language(lang: str) -> str:
    """Maps scraper languages to Notion's strict supported list."""
    if not lang: return "plain text"
    
    clean = lang.lower().strip()
    
    mapping = {
        "curl": "bash", "shell": "bash", "sh": "bash", "zsh": "bash",
        "json": "json", "js": "javascript", "javascript": "javascript", "node": "javascript",
        "python": "python", "py": "python", "html": "html", "css": "css",
        "java": "java", "go": "go", "ruby": "ruby", "php": "php", "sql": "sql",
        "xml": "xml", "yaml": "yaml", "yml": "yaml", "c++": "c++", "cpp": "c++",
        "c#": "c#", "csharp": "c#", "default": "plain text", "text": "plain text"
    }
    
    if clean in mapping: return mapping[clean]
    if "curl" in clean: return "bash"
    return "plain text"

async def publish_to_notion():
    if not NOTION_TOKEN or not PAGE_ID:
        logger.error("❌ Missing Credentials. Please check your .env file.")
        return
    if not os.path.exists(INPUT_FILE):
        logger.error(f"❌ File not found: {INPUT_FILE}. Run main.py first.")
        return

    logger.info("🚀 Connecting to Notion...")
    notion = AsyncClient(auth=NOTION_TOKEN)

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    logger.info(f"📖 Loaded {len(data)} sections. Starting upload...")

    for i, item in enumerate(data):
        section_title = item.get("section", "Untitled")
        raw_text = item.get("raw_text", "")
        code_samples = item.get("code_samples", [])

        children = []

        # A. Heading
        children.append({
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [{"type": "text", "text": {"content": section_title[:2000]}}]
            }
        })

        # B. Text (Chunked)
        if raw_text:
            chunks = chunk_text(raw_text)
            for chunk in chunks:
                children.append({
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [{"type": "text", "text": {"content": chunk}}]
                    }
                })

        # C. Code Blocks (Chunked + Normalized)
        for sample in code_samples:
            content = sample.get("code", "") if isinstance(sample, dict) else str(sample)
            raw_lang = sample.get("language", "text") if isinstance(sample, dict) else "text"
            
            if not content: continue

            notion_lang = normalize_language(raw_lang)
            code_chunks = chunk_text(content)
            
            for chunk in code_chunks:
                children.append({
                    "object": "block",
                    "type": "code",
                    "code": {
                        "language": notion_lang,
                        "rich_text": [{"type": "text", "text": {"content": chunk}}]
                    }
                })

        children.append({"object": "block", "type": "divider", "divider": {}})

        # 4. Push to Notion (BATCHED to respect 100-block limit)
        try:
            # Split children list into batches of 100
            batch_size = 100
            for j in range(0, len(children), batch_size):
                batch = children[j:j + batch_size]
                await notion.blocks.children.append(block_id=PAGE_ID, children=batch)
            
            logger.success(f"   [{i+1}/{len(data)}] ✅ Uploaded: {section_title}")
            await asyncio.sleep(0.4) 

        except Exception as e:
            logger.warning(f"   ⚠️ Failed to upload '{section_title}': {e}")

    logger.info("\n🎉 Notion Upload Complete! Check your page.")

if __name__ == "__main__":
    asyncio.run(publish_to_notion())