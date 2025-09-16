text = input()
a = ''

for i in range(len(text)):
    a = a+text[len(text)-i-1]
    
print(a)
