a = input()
b = input()
c = input()
s = set()
for i in a:
    if i not in b and i not in c:
        s.add(i)
for k in b:
    if k not in a and k not in c:
        s.add(k)
for g in c:
    if g not in b and g not in a:
        s.add(g)
print(s)
