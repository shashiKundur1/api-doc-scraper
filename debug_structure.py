import asyncio
from playwright.async_api import async_playwright

async def debug_layout():
    url = "https://docs.firmable.com/api-reference/endpoint/company-get"
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1400, "height": 1000})
        await page.goto(url, wait_until="domcontentloaded")
        await page.wait_for_timeout(4000) # Wait for layout to settle

        print(f"\n📏 Analyzing Page Layout: {url}")

        # Execute JavaScript to find the largest visible containers
        candidates = await page.evaluate("""() => {
            const elements = document.querySelectorAll('div, main, section, article');
            const results = [];
            
            elements.forEach(el => {
                const rect = el.getBoundingClientRect();
                // Filter out invisible or tiny elements
                if (rect.width < 300 || rect.height < 300) return;
                
                // Calculate Area
                const area = rect.width * rect.height;
                
                // Get clean text snippet
                let text = el.innerText || "";
                text = text.replace(/\\n/g, " ").substring(0, 80);

                results.push({
                    tagName: el.tagName.toLowerCase(),
                    className: el.className,
                    id: el.id,
                    area: area,
                    text: text
                });
            });

            // Sort by Area (Largest first) and take top 5
            return results.sort((a, b) => b.area - a.area).slice(0, 5);
        }""")

        print("\n🏆 Top 5 Largest Containers (Candidates for Main Content):")
        print("-" * 60)
        for i, c in enumerate(candidates):
            class_str = f" class='{c['className']}'" if c['className'] else ""
            id_str = f" id='{c['id']}'" if c['id'] else ""
            
            print(f"{i+1}. <{c['tagName']}{id_str}{class_str}>")
            print(f"   📐 Area: {int(c['area']):,} px")
            print(f"   📝 Text: \"{c['text']}...\"")
            print("-" * 60)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(debug_layout())