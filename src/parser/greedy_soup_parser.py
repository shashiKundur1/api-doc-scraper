from bs4 import BeautifulSoup, Tag
from src.utils.logger import logger

class GreedySoupParser:
    def parse_html(self, html_content: str):
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # 1. Target the Main Content
        # ContactOut uses .content. If missing, fall back to body.
        content_div = soup.select_one('.content') or soup.select_one('body')
        
        endpoints = []
        current_endpoint = {
            "heading": "Introduction (Default)",
            "description": "",
            "code_samples": [],
            "params": []
        }

        # 2. Linear Scan: Iterate over EVERY element in document order
        # We search specifically for the elements we care about to maintain order
        all_elements = content_div.find_all(['h1', 'h2', 'p', 'pre', 'table', 'blockquote'])
        
        logger.info(f"Scanning {len(all_elements)} elements linearly...")

        for tag in all_elements:
            # A. HEADERS: Start a new section
            if tag.name in ['h1', 'h2']:
                # Save previous section (if it has data)
                if current_endpoint["code_samples"] or current_endpoint["params"] or len(current_endpoint["description"]) > 50:
                    endpoints.append(current_endpoint)
                
                # Reset for new section
                current_endpoint = {
                    "heading": tag.get_text(strip=True),
                    "description": "",
                    "code_samples": [],
                    "params": []
                }

            # B. CODE: Grab everything. No filters.
            elif tag.name == 'pre':
                code_text = tag.get_text(strip=True)
                if code_text:
                    # Capture formatting class if available (e.g., 'python', 'curl')
                    classes = tag.get('class', [])
                    lang = "text"
                    if any('curl' in str(c).lower() for c in classes): lang = "curl"
                    elif any('json' in str(c).lower() for c in classes): lang = "json"
                    
                    current_endpoint["code_samples"].append({
                        "language": lang,
                        "raw_html": str(tag), # Save raw HTML just in case
                        "code": code_text
                    })

            # C. TABLES: Parameters
            elif tag.name == 'table':
                rows = []
                for tr in tag.find_all('tr'):
                    cells = [td.get_text(strip=True) for td in tr.find_all(['td', 'th'])]
                    if cells:
                        rows.append(cells)
                if rows:
                    current_endpoint["params"].append(rows)

            # D. DESCRIPTION: Accumulate text
            elif tag.name in ['p', 'blockquote']:
                text = tag.get_text(strip=True)
                if text:
                    current_endpoint["description"] += text + "\n\n"

        # Save the final section
        endpoints.append(current_endpoint)
        
        return endpoints