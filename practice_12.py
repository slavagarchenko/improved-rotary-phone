# 1
text = input('текст: ')
k = 0
f = 0
for i in range(len(text)):
    if text[i] == ' ':
        f += 1
    k = max(f, k)
print(k)
