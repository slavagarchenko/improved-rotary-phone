text = input()
k = set()
words = text.split()
clean_words = []

for word in words:
    cleaned = word.rstrip('.,!?;:')  # удаление символа на конце слова
    clean_words.append(cleaned)
    
for i in clean_words:
    if i in k:
        print(i)
    else:
        k.add(i)
