

with open('min_text2', encoding='utf-8') as f:
    for line in f:
        print(f"{line.strip()} <har längden {len(line)}")

