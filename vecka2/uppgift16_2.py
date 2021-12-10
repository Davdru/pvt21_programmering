

f = open('min_text2')

for line in f:
    print(f"{line.strip()} <har längden {len(line)}")


f.close()
