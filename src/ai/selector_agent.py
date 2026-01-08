from openai import AsyncOpenAI
from pydantic import BaseModel, Field
from config.settings import settings
from src.utils.logger import logger

class ScraperSelectors(BaseModel):
    sidebar_selector: str = Field(..., description="CSS selector for sidebar navigation links")
    content_selector: str = Field(..., description="CSS selector for the main content area")
    endpoint_selector: str = Field(..., description="CSS selector for individual API endpoint blocks")
    title_selector: str = Field(..., description="CSS selector for the endpoint title/heading")
    description_selector: str = Field(..., description="CSS selector for the endpoint description")
    code_block_selector: str = Field(..., description="CSS selector for code snippet blocks")
    parameter_table_selector: str = Field(..., description="CSS selector for the parameters table or list")

class SelectorAgent:
    def __init__(self):
        self.client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = "gpt-4o" # Must use a smart model for this

    async def analyze_page_structure(self, html_snippet: str) -> ScraperSelectors:
        """
        Analyzes raw HTML to identify the correct CSS selectors for scraping.
        """
        logger.info("🕵️ Asking AI to identify CSS selectors from HTML structure...")
        
        system_prompt = (
            "You are a Senior QA Engineer. Your job is to identify robust CSS selectors from an HTML snippet. "
            "Return a JSON object with the CSS selectors needed to scrape this API documentation. "
            "Focus on 'role', 'class', or 'id' attributes. Avoid long, brittle chains."
        )

        try:
            completion = await self.client.beta.chat.completions.parse(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Analyze this HTML and find the selectors:\n\n{html_snippet}"},
                ],
                response_format=ScraperSelectors,
            )
            return completion.choices[0].message.parsed
        except Exception as e:
            logger.error(f"Selector Agent failed: {e}")
            return None