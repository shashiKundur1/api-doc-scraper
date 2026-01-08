import json
import re
from typing import List, Optional, Type
from pydantic import BaseModel, Field, ValidationError
from openai import AsyncOpenAI
from config.settings import settings
from src.utils.logger import logger

# --- 1. Schema Definitions (Unchanged) ---
class Param(BaseModel):
    name: str = Field(..., description="Name of the parameter")
    type: str = Field(..., description="Data type")
    required: bool = Field(..., description="Is this required?")
    description: Optional[str] = Field(None, description="Description")

class CodeSample(BaseModel):
    language: str = Field(..., description="Language (curl, python, node)")
    code: str = Field(..., description="The exact code snippet")

class Request(BaseModel):
    method: str = Field(..., description="HTTP Method")
    endpoint: str = Field(..., description="API Endpoint path")
    payload_sample: Optional[str] = Field(None, description="Stringified JSON payload")
    code_samples: List[CodeSample] = Field(default_factory=list, description="Code examples")

class Response(BaseModel):
    status_code: int = Field(..., description="HTTP Status Code")
    description: str = Field(..., description="Outcome description")
    body_sample: Optional[str] = Field(None, description="Stringified JSON body")

class ApiEndpoint(BaseModel):
    heading: str = Field(..., description="Endpoint title")
    description: str = Field(..., description="Detailed explanation")
    params: List[Param] = Field(default_factory=list, description="Parameters")
    request: Optional[Request] = Field(None, description="Request details")
    responses: List[Response] = Field(default_factory=list, description="Responses")

class DocumentationData(BaseModel):
    endpoints: List[ApiEndpoint] = Field(..., description="All extracted endpoints")

# --- 2. Upgraded AI Processor (Supports o1-preview & gpt-4o) ---

class GptProcessor:
    def __init__(self, model: str = "gpt-4o"): 
        self.client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = model

    async def process_content(self, clean_text: str) -> DocumentationData:
        """
        Extracts structured data using either GPT-4o (Standard) or o1-preview (High Reasoning).
        """
        # Safety truncation
        if len(clean_text) > 100000:
            logger.warning(f"⚠️ Truncating text to 100,000 chars.")
            clean_text = clean_text[:100000]

        logger.info(f"🧠 Sending {len(clean_text)} chars to {self.model}...")

        # --- LOGIC BRANCH: o1-preview vs gpt-4o ---
        if self.model.startswith("o1"):
            return await self._process_with_o1(clean_text)
        else:
            return await self._process_with_gpt4o(clean_text)

    async def _process_with_gpt4o(self, clean_text: str) -> DocumentationData:
        """Standard processing for GPT-4o using Structured Outputs."""
        system_prompt = (
            "You are a Data Extraction Engine. Extract EXHAUSTIVE API documentation. "
            "1. Extract ALL parameters and fields. "
            "2. Extract ALL code samples exactly as written (curl, python, etc). "
            "3. Do not summarize."
        )
        try:
            completion = await self.client.beta.chat.completions.parse(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": clean_text},
                ],
                response_format=DocumentationData,
                temperature=0.0,
            )
            result = completion.choices[0].message.parsed
            logger.success(f"🧠 AI Successfully extracted {len(result.endpoints)} endpoints.")
            return result
        except Exception as e:
            logger.error(f"GPT-4o Error: {e}")
            return DocumentationData(endpoints=[])

    async def _process_with_o1(self, clean_text: str) -> DocumentationData:
        """
        Special processing for o1-preview / o1-mini.
        o1 models do NOT support 'system' role or 'response_format' yet.
        We must prompt-engineer a raw JSON response.
        """
        # Combine system instructions into the User prompt
        prompt = (
            "You are an expert API Documentation Parser. Your task is to extract structured API data from the text below.\n\n"
            "STRICT OUTPUT RULES:\n"
            "1. Return ONLY a valid JSON object matching this schema:\n"
            "{ 'endpoints': [ { 'heading': str, 'description': str, 'params': [], 'request': {...}, 'responses': [] } ] }\n"
            "2. Do not include markdown formatting (like ```json). Just the raw JSON string.\n"
            "3. Extract ALL code samples into 'code_samples'.\n"
            "4. Be exhaustive. Do not summarize.\n\n"
            f"--- DOCUMENTATION TEXT ---\n{clean_text}"
        )

        try:
            # o1 models usually require high max_completion_tokens
            completion = await self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}]
            )

            raw_content = completion.choices[0].message.content
            
            # Clean potential markdown wrapping
            raw_content = self._clean_json_string(raw_content)
            
            # Parse manually
            data_dict = json.loads(raw_content)
            result = DocumentationData(**data_dict)
            
            logger.success(f"🧠 o1-Reasoning Successfully extracted {len(result.endpoints)} endpoints.")
            return result

        except Exception as e:
            logger.error(f"o1-Reasoning Error: {e}")
            # Fallback: Try to rescue partial JSON if possible, or return empty
            return DocumentationData(endpoints=[])

    def _clean_json_string(self, text: str) -> str:
        """Removes markdown code blocks if the model adds them."""
        text = text.strip()
        if text.startswith("```json"):
            text = text[7:]
        if text.startswith("```"):
            text = text[3:]
        if text.endswith("```"):
            text = text[:-3]
        return text.strip()