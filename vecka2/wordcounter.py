
words = {}

f = open('lorem.txt', encoding='utf8')
for line in f:
    words_in_line = line.split()
    for w in words_in_line:
        if w in words:
            words[w] += 1
        else:
            words[w] = 1




print(sorted(words, key=words.get))
print(words['the'])