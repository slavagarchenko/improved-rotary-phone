import re
text = input()
found  = None

for item in set(text):
    symbol = re.escape(item)
    count = len(re.findall(symbol, text))
    
    if count == 3:
        found = item
        break
        
if found is not None:
    print(found)
    
else:
    print("None")
