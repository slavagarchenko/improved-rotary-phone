text = input()
words = text.split()
first = words[0]
a = []

for word in words[1:]:
    cleaned = word.rstrip(".,!?:;")
    # set(cleaned)-создает множетсво состоящее из букв слова
    if cleaned != first and len(set(cleaned)) == len(cleaned):
        a.append(cleaned)
      
print(a)
