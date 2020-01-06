text = input().split()
for a in range(len(text)):
    if len(text[a]) > 3:
        if text[a][0:1] == text[a][2:3]:
            text[a] = text[a][2:]

text = ' '.join(text)
print(text)
