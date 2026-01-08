import json

def inspect():
    with open("output/raw_scrape_data.json", "r") as f:
        data = json.load(f)

    print(f"📉 Loaded {len(data)} sections.\n")
    
    # Check first 3 sections
    for i in range(3):
        section = data[i]
        print(f"--- SECTION: {section['section']} ---")
        print(f"Length of Text: {len(section['raw_text'])} chars")
        print(f"Code Samples: {len(section['code_samples'])}")
        print(f"Sample Text: {section['raw_text'][:100]}...\n")

    # Check for duplication
    if data[0]['raw_text'] == data[1]['raw_text']:
        print("⚠️ CRITICAL ALERT: The content is IDENTICAL across sections.")
        print("The scraper grabbed the whole page each time. We need to perform 'NLP Slicing'.")
    else:
        print("✅ Data looks unique per section.")

if __name__ == "__main__":
    inspect()