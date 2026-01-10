import os
from src.utils.logger import logger

class MarkdownGenerator:
    @staticmethod
    def generate_doc(data_list: list, output_file: str):
        """
        Generates Markdown from the Non-AI Scraper output (list of dicts).
        """
        logger.info(f"✨ Generating Markdown from {len(data_list)} sections...")
        
        md = []
        md.append("# Firmable API Documentation\n")
        md.append("> **Generated via Copy-Button Detection**\n---\n")

        for item in data_list:
            # Handle Dictionary access (Fixes AttributeError)
            section_name = item.get("section", "Untitled")
            raw_text = item.get("raw_text", "")
            code_samples = item.get("code_samples", [])

            md.append(f"## {section_name}\n")
            
            # Clean up text (remove excessive newlines)
            clean_text = raw_text.strip()
            if clean_text:
                md.append(f"{clean_text}\n")

            # Code Samples
            if code_samples:
                md.append("#### 💻 Code Samples")
                for i, sample in enumerate(code_samples):
                    # Sample is a dict: {'language': 'bash', 'code': '...'}
                    lang = sample.get("language", "text")
                    code = sample.get("code", "")
                    
                    md.append(f"**Block {i+1} ({lang})**")
                    md.append(f"```{lang}\n{code}\n```\n")
            
            md.append("---\n")

        # Save to file
        try:
            os.makedirs(os.path.dirname(output_file), exist_ok=True)
            with open(output_file, "w", encoding="utf-8") as f:
                f.write("\n".join(md))
            
            logger.success(f"✅ Markdown saved to: {output_file}")
        except Exception as e:
            logger.error(f"❌ Failed to save markdown: {e}")