import re
import tiktoken
from config.settings import settings
from src.utils.logger import logger

class Cleaner:
    """
    Utilities to clean Markdown and optimize tokens for LLM ingestion.
    Implements 2025 best practices for RAG/Context preparation.
    """

    @staticmethod
    def clean_markdown(text: str) -> str:
        """
        Removes documentation noise (links, TOCs, footers) to save tokens.
        """
        logger.info("Cleaning markdown content...")
        initial_len = len(text)

        # 1. Remove "Edit on GitHub" / "View Source" links
        patterns_to_remove = [
            r'\[.*?[Ee]dit.*?[Gg]ithub.*?\]\([^)]+\)',
            r'\[.*?[Vv]iew.*?[Ss]ource.*?\]\([^)]+\)',
            r'Last updated.*?(\n|$)',
            r'Last modified.*?(\n|$)',
        ]
        for pattern in patterns_to_remove:
            text = re.sub(pattern, '', text, flags=re.IGNORECASE)

        # 2. Remove Table of Contents (TOC)
        # Matches "## Table of Contents" followed by list of links
        toc_pattern = r'^#+\s+(?:Table of )?Contents?\s*\n(?:\s*[-*]\s+\[.*?\]\(#.*?\)\n)*'
        text = re.sub(toc_pattern, '', text, flags=re.MULTILINE | re.IGNORECASE)

        # 3. Flatten Links (Keep text, remove URL)
        # [Click here](https://...) -> Click here
        # Exception: Keep links that might be API endpoints (heuristic)
        text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)

        # 4. Normalize Whitespace
        # Replace 3+ newlines with 2 (one blank line)
        text = re.sub(r'\n{3,}', '\n\n', text)
        
        # 5. Trim lines
        text = '\n'.join([line.strip() for line in text.split('\n')])

        final_len = len(text)
        saved = initial_len - final_len
        logger.info(f"Cleaning complete. Reduced size by {saved} chars ({saved/initial_len:.1%}%)")
        
        return text

    @staticmethod
    def count_tokens(text: str) -> int:
        """
        Counts tokens using tiktoken (OpenAI standard).
        Uses 'cl100k_base' which is used by gpt-4o-mini / gpt-3.5-turbo.
        """
        try:
            encoding = tiktoken.get_encoding("cl100k_base")
            return len(encoding.encode(text))
        except Exception as e:
            logger.warning(f"Token counting failed: {e}")
            return len(text) // 4  # Rough fallback

    @staticmethod
    def truncate_to_token_limit(text: str, max_tokens: int = 120000) -> str:
        """
        Truncates text to fit within context window limits.
        GPT-4o-mini has 128k context, so we set a safe buffer.
        """
        tokens = Cleaner.count_tokens(text)
        if tokens <= max_tokens:
            return text
        
        logger.warning(f"Text exceeds token limit ({tokens} > {max_tokens}). Truncating...")
        encoding = tiktoken.get_encoding("cl100k_base")
        encoded = encoding.encode(text)
        truncated = encoded[:max_tokens]
        return encoding.decode(truncated)