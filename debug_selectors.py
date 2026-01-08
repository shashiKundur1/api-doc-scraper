import asyncio
from playwright.async_api import async_playwright

async def debug_page_structure():
    # Target a specific endpoint page that definitely has code
    url = "https://api.contactout.com/#email-search" 
    print(f"🕵️‍♀️ Inspecting Structure for: {url}")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        await page.goto(url, wait_until="networkidle")
        await page.wait_for_timeout(3000)

        print("\n--- 1. FINDING CODE BLOCKS ---")
        # Find any element containing "curl" (case insensitive)
        code_elements = await page.locator("text=/curl/i").all()
        
        if code_elements:
            print(f"✅ Found {len(code_elements)} elements containing 'curl'. Analyzing parent structure...")
            for i, el in enumerate(code_elements[:3]):
                # Get the class and tag of the parent
                parent = el.locator("..")
                tag = await parent.evaluate("el => el.tagName")
                classes = await parent.get_attribute("class")
                print(f"   Match {i}: Parent is <{tag} class='{classes}'>")
                
                # Check for <pre> or <code> nearby
                pre_tag = page.locator("pre").first
                if await pre_tag.count() > 0:
                    pre_class = await pre_tag.get_attribute("class")
                    print(f"   💡 Found global <pre> tag with class: '{pre_class}'")
        else:
            print("❌ No text 'curl' found. Trying 'pre' tag directly...")
            count = await page.locator("pre").count()
            print(f"   Found {count} <pre> tags.")
            if count > 0:
                first_pre = page.locator("pre").first
                print(f"   First <pre> class: {await first_pre.get_attribute('class')}")

        print("\n--- 2. FINDING MAIN CONTENT ---")
        # Try to find the container
        for selector in [".content", "#content", "main", "article", ".documentation"]:
            count = await page.locator(selector).count()
            if count > 0:
                print(f"   ✅ Container candidate: '{selector}' (Found {count})")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(debug_page_structure())