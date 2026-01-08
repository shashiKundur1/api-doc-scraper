from bs4 import BeautifulSoup, Tag
import json
from src.utils.logger import logger

class SoupParser:
    def parse_html(self, html_content: str):
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # 1. Locate the Main Content Container
        # Slate/ContactOut puts content in '.content'
        content_div = soup.select_one('.content')
        if not content_div:
            logger.error("Could not find .content div. Checking for alternatives...")
            content_div = soup.select_one('body') # Fallback
            
        endpoints = []
        
        # 2. Find all Section Headers (The "Anchors")
        # We look for H1 and H2 as they usually denote major sections
        headers = content_div.find_all(['h1', 'h2'])
        
        logger.info(f"Found {len(headers)} sections to slice.")

        for i, header in enumerate(headers):
            section_title = header.get_text(strip=True)
            
            # Initialize Data Containers for THIS section
            description_parts = []
            code_samples = []
            params = []
            
            # 3. The "Slicing" Loop
            # Look at all siblings after this header until we hit the next header
            curr = header.next_sibling
            
            while curr:
                # STOP if we hit the next major header
                if isinstance(curr, Tag) and curr.name in ['h1', 'h2']:
                    break
                
                # PROCESS contents
                if isinstance(curr, Tag):
                    # A. Code Blocks (Slate puts them in pre.highlight)
                    # We look for <pre> tags explicitly
                    pres = curr.find_all('pre')
                    if curr.name == 'pre': pres.append(curr)
                    
                    for pre in pres:
                        code_text = pre.get_text(strip=True)
                        if len(code_text) > 5: # Filter empty noise
                            # Guess language from class
                            classes = pre.get('class', [])
                            lang = "text"
                            if any('python' in c for c in classes): lang = "python"
                            elif any('curl' in c or 'shell' in c for c in classes): lang = "curl"
                            elif any('javascript' in c or 'json' in c for c in classes): lang = "javascript"
                            
                            code_samples.append({
                                "language": lang,
                                "code": code_text
                            })

                    # B. Parameters Tables
                    if curr.name == 'table':
                        rows = curr.find_all('tr')
                        for row in rows:
                            cols = row.find_all(['td', 'th'])
                            if len(cols) >= 2:
                                clean_cols = [c.get_text(strip=True) for c in cols]
                                params.append({
                                    "name": clean_cols[0],
                                    "type": clean_cols[1] if len(clean_cols) > 1 else "string",
                                    "description": clean_cols[-1] if len(clean_cols) > 0 else ""
                                })

                    # C. Text Description (Paragraphs, Blockquotes, Lists)
                    if curr.name in ['p', 'ul', 'ol', 'aside', 'blockquote']:
                        text = curr.get_text(strip=True)
                        if text:
                            description_parts.append(text)

                # Move to next sibling
                curr = curr.next_sibling

            # 4. Construct Endpoint Object
            if section_title:
                endpoints.append({
                    "heading": section_title,
                    "description": "\n\n".join(description_parts),
                    "params": params,
                    "code_samples": code_samples
                })
                
        return endpoints