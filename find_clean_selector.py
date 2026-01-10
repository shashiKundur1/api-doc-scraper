import asyncio
from playwright.async_api import async_playwright

async def find_clean_selector():
    url = "https://docs.firmable.com/api-reference/endpoint/company-get"
    target_text = "Returns company information" # Unique text in the middle column
    bad_text = "Firmable home page"           # Text in the sidebar/header we want to AVOID

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url, wait_until="domcontentloaded")
        await page.wait_for_timeout(3000)

        print(f"🎯 Hunting for container with: '{target_text}'")
        print(f"⛔ Must NOT contain: '{bad_text}'\n")

        # 1. Find the text element
        element = page.get_by_text(target_text, exact=False).first
        
        if not await element.count():
            print("❌ Could not find target text. Page might not have loaded.")
            await browser.close()
            return

        # 2. Walk up the tree
        current = element
        for i in range(10): # Check 10 levels up
            tag = await current.evaluate("el => el.tagName.toLowerCase()")
            class_attr = await current.get_attribute("class") or ""
            id_attr = await current.get_attribute("id") or ""
            
            # Get all text in this container
            full_text = await current.inner_text()
            
            print(f"Level {i}: <{tag} id='{id_attr}' class='{class_attr[:50]}...'>")
            
            if bad_text in full_text:
                print(f"   ❌ CONTAINS BAD TEXT (Sidebar/Header detected!) - STOPPING HERE.")
                break
            else:
                print(f"   ✅ CLEAN! (Contains target, excludes sidebar)")
                print(f"   👍 Selector candidate: {tag}.{class_attr.replace(' ', '.')}")
                # Save this locator for the user
                best_selector = f"{tag}[class='{class_attr}']" if class_attr else tag
            
            # Move to parent
            current = current.locator("..")
            print("-" * 40)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(find_clean_selector())