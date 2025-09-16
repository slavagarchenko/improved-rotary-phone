text = input('текст: ')
k = 0
f = 0
for i in range(len(text)-1):
    if text[i] == ' ':
        f += 1
    if text[i+1] != ' ':
        k = max(f, k)
        f = 0
print(k)
