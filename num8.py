sentence = input()
words = []

for word in sentence.split():
    cleaned = word.rstrip('.,!?;:')  # удаление символа на конце слова
    words.append(cleaned)
  
for word in sorted(words, key=len):
    print(word)
