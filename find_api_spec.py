import asyncio
from playwright.async_api import async_playwright

async def find_api_spec():
    # TEST URL: Change this to the site you want to test (e.g., https://api.contactout.com/)
    url = "https://api.contactout.com/" 
    print(f"🕵️‍♀️ Sniffing Network Traffic for API Specs on: {url}")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # List to store potential API spec files
        found_specs = []

        # 1. Listen to all network requests
        page.on("request", lambda request: check_request(request, found_specs))

        # 2. Go to the page and wait for everything to load
        try:
            await page.goto(url, wait_until="networkidle", timeout=15000)
            await page.wait_for_timeout(5000) # Wait extra time for background fetches
        except Exception as e:
            print(f"Navigation warning: {e}")

        print("\n--- ANALYSIS COMPLETE ---")
        if found_specs:
            print(f"✅ JACKPOT! Found {len(found_specs)} potential API Spec files:")
            for spec in found_specs:
                print(f"   📂 {spec}")
            print("\nRecommendation: We can download this JSON/YAML directly. No AI needed.")
        else:
            print("❌ No direct API spec file found. We must fallback to 'Agentic DOM Slicing'.")

        await browser.close()

def check_request(request, found_specs):
    url = request.url.lower()
    # Look for common OpenAPI/Swagger file patterns
    if any(x in url for x in [".json", ".yaml", ".yml"]) and \
       any(y in url for y in ["swagger", "openapi", "api-docs", "redoc", "spec", "definition"]):
        
        # Filter out random JS/CSS files or analytics
        if "package.json" not in url and "manifest.json" not in url and "google" not in url:
            if url not in found_specs:
                found_specs.append(url)
                print(f"   Found candidate: {url}")

if __name__ == "__main__":
    asyncio.run(find_api_spec())