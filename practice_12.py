# 1
text = input('текст: ')
k = 0
f = 0
for i in range(len(text)-1):
    if text[i] == ' ':
        f += 1
    if text[i+1] != ' ':
        k = max(f, k)
        f = 0
print(k)

# 2
text = input()
count = 1
k = 1
for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        k += 1
    else:
        count = max(count, k)
        k = 1
count = max(count, k)
print(count)

# 3
text = input()
k = set()
for i in range(len(text)):
    if text[i] != ' ':
        k.add(text[i])
print(len(k))

# 4
import re
text = input()
for item in set(text):
    symbol = re.escape(item)
    count = len(re.findall(symbol, text))
    if count == 3:
        print(item)
    else:
        print("None")

# 5
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

# 6
text = input()
a = ''
for i in range(len(text)):
    a = a+text[len(text)-i-1]
print(a)

# 7
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

# 8
sentence = input()
words = []
for word in sentence.split():
    cleaned = word.rstrip('.,!?;:')  # удаление символа на конце слова
    words.append(cleaned)
for word in sorted(words, key=len):
    print(word)

# 9
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

# 10
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

# 11
text = input()
words = text.split()
a = ''

for i in range(1, len(words)):
    if words[i-1][-1].lower() != words[i][0].lower():  # lower() для регистра
        if i % 2 == 1:  # четное по счету слово
            a = 'выиграл Вася'  # Вася нарушил правила
            break
        else:  # нечетное по счету слово
            a = 'выиграл Петя'  # Петя нарушил правила
            break

if a == '':
    if len(words) % 2 == 1:  # последний Петя
        a = 'выиграл Петя'
    else:  # последний Вася
        a = 'выиграл Вася'

print(a)

# 12
import keyword
text = input()
# метод строк который проверяет первый символ - буква, подчеркивание, и отсальные - буквы, цифры, подчеркивании
# функция которая выдает буллинговоые значения (True/False)
if text.isidentifier() and not keyword.iskeyword(text):
    print('может быть именем')
else:
    print('не может быть именем')

# 13
count = 1
while True:
    bilet = input().strip()
    if len(bilet) % 2 == 0:
        first_half_sum = 0
        second_half_sum = 0
        half = len(bilet)//2
        for i in range(half):
            first_half_sum += int(bilet[i])
        for i in range(half, len(bilet)):
            second_half_sum += int(bilet[i])
        if first_half_sum == second_half_sum:
            print(count)
            break
    count += 1

# 14
hint = input("Подсказка: ")
word = input("Загаданное слово").lower()
zv = '*'*len(word)
letters = set()
attempts = 10

print('\n'*25)
print("Подсказка: ", hint)
print(zv)

while attempts > 0:
    print("Осталось попыток: ", attempts)

    try:
        answer = int(input('Буква или слово(0-буква, 1-слово)? '))
    except ValueError:
        print("Пожалуйста, введите 0-буква или 1-слово")
        continue

    if answer == 0:
        bukva = input("Введите букву: ").lower()
        if len(bukva) != 1:
            print("Введите одну букву")
            continue
        if not bukva.isalpha():
            print("Введите букву")
            continue
        if bukva in letters:
            print("Вы уже называли эту букву")
            continue

        letters.add(bukva)

        if bukva in word:
            new_zv = list(zv)
            for i in range(len(word)):
                if word[i] == bukva:
                    new_zv[i] = bukva
            zv = ''.join(new_zv)
            print(zv)

            if zv == word:
                print('Победа!')
                break
        else:
            attempts -= 1
            print("Такой буквы нет")
            print("Слово: ", zv)

    elif answer == 1:
        slovo = input("Введите слово").lower()
        if slovo == word:
            print('Победа!')
            break
        else:
            attempts -= 1
            print('Проигрыш!')
        if attempts == 0:
            print("Проигрыш")
        break

    else:
        print("Введите 0 или 1")

    if attempts == 0:
        print("Проигрыш")
        print("Загаданное слово: ", word)
        break

# 15
secret = input("Введите четырёхзначное число с неповторяющимися цифрами: ")
while len(secret) != 4 or not secret.isdigit() or len(set(secret)) != 4:
    secret = input("Ошибка! Повторите ввод: ")

print('\n' * 25)
print("Игра началась! У вас 10 попыток.\n")

for i in range(1, 11):
    while True:
        print("Попытка №", i)
        guess = input("Введите число: ")

        if len(guess) != 4 or not guess.isdigit():
            print("Ошибка! Введите четырёхзначное число.")
            continue

        if len(set(guess)) != 4:
            print("Ошибка! Цифры в числе не должны повторяться.")
            continue

        break

    bulls = 0
    cows = 0

    for k in range(4):
        if guess[k] == secret[k]:
            bulls += 1
        elif guess[k] in secret:
            cows += 1

    print(f"Быки: {bulls}, Коровы: {cows}")

    if bulls == 4:
        print("Победа!")
        break
    else:
        remaining_attempts = 10 - i
        print("Осталось попыток: ", remaining_attempts)
        print("-"*30)

else:
    print("Проигрыш!")
    print("Загаданное число было:", secret)

# 16
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

# 18
def justify(text, width):
    words = text.split()
    lines = []
    current_line = []

    current_len = 0
    for word in words:  # проверка места для слова
        # + len(current_line) - пробелы между словами
        if current_len + len(word) + len(current_line) <= width:
            current_line.append(word)
            current_len += len(word)
        else:
            line = align_line(current_line, width)
            lines.append(line)
            current_line = [word]
            current_len = len(word)
    if current_line:
        lines.append(" ".join(current_line))

    return "\n".join(lines)


def align_line(words, width):
    if len(words) == 1:
        return words[0].ljust(width)

    total_chars = sum(len(word) for word in words)  # общая длина слов
    spaces_needed = width - total_chars  # кол-во пробелов
    gaps = len(words) - 1  # кол-во промежутков между словами
    space_between = spaces_needed // gaps  # база пробелов
    extra_spaces = spaces_needed % gaps  # лишние пробелы

    line = ""
    for i, word in enumerate(words[:-1]):
        line += word + " " * (space_between + (1 if i < extra_spaces else 0))
    line += words[-1]
    return line


text = input("Введите текст: ")
width = int(input("Введите ширину колонки: "))

justified = justify(text, width)
print("\nОтформатированный текст:\n")
print(justified)

# 20
def number_to_words(n):
    units = ["", "один", "два", "три", "четыре",
             "пять", "шесть", "семь", "восемь", "девять"]
    teens = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать",
             "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят",
            "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    hundreds = ["", "сто", "двести", "триста", "четыреста",
                "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]

    def convert(num, is_female=False):
        hu = num // 100  # сотни
        te = (num % 100)//10  # десятки
        un = num % 10  # единицы

        result = []

        if hu > 0:
            result.append(hundreds[hu])
        if te == 1:
            result.append(teens[un])
        else:
            if te > 0:
                result.append(tens[te])
            if un > 0:
                if is_female and un in [1, 2]:
                    result.append("одна" if un == 1 else "две")
                else:
                    result.append(units[un])

        return " ".join(result)

    def get_form(number, forms):
        if 11 <= number % 100 <= 14:
            return forms[2]
        elif number % 10 == 1:
            return forms[0]
        elif 2 <= number % 10 <= 4:
            return forms[1]
        else:
            return forms[2]

    if n == 0:
        return "ноль"

    millions = n//1_000_000
    thousands = (n % 1_000_000)//1_000
    units_part = n % 1_000

    parts = []

    if millions > 0:
        parts.append(convert(millions))
        parts.append(get_form(millions, ["миллион", "миллиона", "миллионов"]))

    if thousands > 0:
        parts.append(convert(thousands, is_female=True))
        parts.append(get_form(thousands, ["тысяча", "тысячи", "тысяч"]))

    if units_part > 0:
        parts.append(convert(units_part))

    return " ".join(parts)


num = int(input("Введите число (до 900000000): "))
if 0 <= num <= 900_000_000:
    print(number_to_words(num))
else:
    print("Число вне диапазона")
