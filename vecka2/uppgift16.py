
# Öppna filen
f = open('min_text2')

# Läs filen så att varje rad blir ett element i en lista
min_text = f.readlines()

# Skriver ut element nummer 2
print(min_text[1])

# Loopa igenom hela listan och skriv ut varje rad med textens längd
for line in min_text:
    print(f"{line.strip()} <har längden {len(line)}")

# Stäng filen efter oss
f.close()
