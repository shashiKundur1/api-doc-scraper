import yaml
import json
import requests
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field
from src.ai.gpt_processor import ApiEndpoint, Param, Request, Response, DocumentationData
from src.utils.logger import logger

# Extend the Pydantic model to support code samples
class CodeSample(BaseModel):
    lang: str
    source: str

# Monkey-patch Request model to include code samples (runtime update)
# In a real app, you'd update the class definition in gpt_processor.py directly
Request.model_rebuild(force=True)

class OpenApiParser:
    def __init__(self, spec_url: str):
        self.spec_url = spec_url
        self.spec = None

    def fetch_spec(self):
        """Downloads and parses the YAML/JSON specification."""
        logger.info(f"📥 Downloading OpenAPI Spec from: {self.spec_url}")
        try:
            response = requests.get(self.spec_url, timeout=10)
            response.raise_for_status()
            try:
                self.spec = yaml.safe_load(response.text)
            except yaml.YAMLError:
                self.spec = json.loads(response.text)
            logger.success("✅ OpenAPI Spec downloaded and parsed successfully.")
            return True
        except Exception as e:
            logger.error(f"Failed to download spec: {e}")
            return False

    def resolve_ref(self, ref: str) -> Dict[str, Any]:
        if not isinstance(ref, str) or not ref.startswith("#/"):
            return {}
        parts = ref.split("/")[1:]
        current = self.spec
        for part in parts:
            current = current.get(part, {})
        return current

    def parse(self) -> DocumentationData:
        if not self.spec:
            if not self.fetch_spec():
                return DocumentationData(endpoints=[])

        endpoints = []
        paths = self.spec.get("paths", {})

        logger.info(f"🔄 Processing {len(paths)} paths...")

        for path, methods in paths.items():
            for method, details in methods.items():
                if method.lower() not in ["get", "post", "put", "delete", "patch"]:
                    continue

                # 1. Basic Info
                heading = details.get("summary") or details.get("operationId") or f"{method.upper()} {path}"
                description = details.get("description", "No description provided.")

                # 2. Parameters
                params_list = []
                if "parameters" in details:
                    for p in details["parameters"]:
                        if "$ref" in p: p = self.resolve_ref(p["$ref"])
                        params_list.append(Param(
                            name=p.get("name", "unknown"),
                            type=p.get("schema", {}).get("type", "string"),
                            required=p.get("required", False),
                            description=p.get("description")
                        ))

                # 3. Request Body & Code Samples
                payload_sample = None
                
                # A. Handle Request Body Schema
                if "requestBody" in details:
                    content = details["requestBody"].get("content", {})
                    json_content = content.get("application/json", {})
                    schema = json_content.get("schema", {})
                    if "$ref" in schema: schema = self.resolve_ref(schema["$ref"])
                    
                    # Generate sample JSON
                    example = self._generate_example(schema)
                    payload_sample = json.dumps(example, indent=2)

                # B. EXTRACT CODE SAMPLES (The new feature!)
                # Redoc uses 'x-code-samples', others might use 'x-examples'
                code_samples = []
                x_samples = details.get("x-code-samples") or details.get("x-examples")
                if x_samples:
                    for sample in x_samples:
                        # Sometimes it's a list of dicts {lang, source}
                        if isinstance(sample, dict):
                            lang = sample.get("lang") or sample.get("language")
                            source = sample.get("source") or sample.get("code")
                            if lang and source:
                                # Append to description or handle differently
                                # Here we append to description for visibility in Markdown
                                description += f"\n\n**Example ({lang}):**\n```\n{source}\n```"

                req_obj = Request(
                    method=method.upper(),
                    endpoint=path,
                    payload_sample=payload_sample
                )

                # 4. Responses
                responses_list = []
                for status, resp_data in details.get("responses", {}).items():
                    if "$ref" in resp_data: resp_data = self.resolve_ref(resp_data["$ref"])
                    
                    body_sample = None
                    if "content" in resp_data:
                        schema = resp_data["content"].get("application/json", {}).get("schema", {})
                        if "$ref" in schema: schema = self.resolve_ref(schema["$ref"])
                        body_sample = json.dumps(self._generate_example(schema), indent=2)

                    responses_list.append(Response(
                        status_code=int(status) if status.isdigit() else 200,
                        description=resp_data.get("description", ""),
                        body_sample=body_sample
                    ))

                endpoints.append(ApiEndpoint(
                    heading=heading,
                    description=description,
                    params=params_list,
                    request=req_obj,
                    responses=responses_list
                ))

        return DocumentationData(endpoints=endpoints)

    def _generate_example(self, schema: Dict[str, Any]) -> Any:
        if "$ref" in schema: schema = self.resolve_ref(schema["$ref"])
        t = schema.get("type")
        if t == "object":
            return {k: self._generate_example(v) for k, v in schema.get("properties", {}).items()}
        if t == "array":
            return [self._generate_example(schema.get("items", {}))]
        if "example" in schema: return schema["example"]
        return schema.get("default", "value")