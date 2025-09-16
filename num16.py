text = input("Введите текст: ")

balance = 0
correct = True

for char in text:
    if char == '(':
        balance += 1
    elif char == ')':
        balance -= 1
        if balance < 0:
            correct = False
            break

if balance != 0:
    correct = False

if correct:
    print("Скобки расставлены правильно.")
else:
    print("Скобки расставлены неправильно.")
