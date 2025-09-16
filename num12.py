import keyword
text = input()
# метод строк который проверяет первый символ - буква, подчеркивание, и отсальные - буквы, цифры, подчеркивании
# функция которая выдает буллинговоые значения (True/False)
if text.isidentifier() and not keyword.iskeyword(text):
    print('может быть именем')
else:
    print('не может быть именем')
