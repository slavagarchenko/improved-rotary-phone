text = input()
count = float('+inf')
k = 0
for i in range(len(text)):
    if text[i] != ' ':
        k += 1
    else:
        count = min(count, k)
        k = 0
print(count)
