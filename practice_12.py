# 1
import pyphen
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
    symbol =  re.escape(item)
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
    cleaned = word.rstrip('.,!?;:')#удаление символа на конце слова
    words.append(cleaned)
for word in sorted(words, key=len):
    print(word)

# 9
text = input()
k = set()
words = text.split()
clean_words = []
for word in words:
    cleaned = word.rstrip('.,!?;:')#удаление символа на конце слова
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
    if cleaned != first and len(set(cleaned)) == len(cleaned):# set(cleaned)-создает множетсво состоящее из букв слова
        a.append(cleaned)
print(a)

# 11
text = input()
words = text.split()
a = ''

for i in range(1, len(words)):
    if words[i-1][-1].lower() != words[i][0].lower():  #lower() для регистра
        if i % 2 == 1:  #четное по счету слово
            a = 'выиграл Вася'  #Вася нарушил правила
            break
        else: #нечетное по счету слово
            a = 'выиграл Петя'  #Петя нарушил правила
            break

if a == '':
    if len(words) % 2 == 1:  #последний Петя
        a = 'выиграл Петя'
    else: #последний Вася
        a = 'выиграл Вася'

print(a)

# 12
import keyword

text = input()
#метод строк который проверяет первый символ - буква, подчеркивание, и отсальные - буквы, цифры, подчеркивании   
if text.isidentifier() and not keyword.iskeyword(text):  #функция которая выдает буллинговоые значения (True/False)
        print('может быть именем')
else:
    print('не может быть именем')
    
# 13
count = 1
s = 0
w = 0
while True:
    bilet = input()
    if len(bilet) % 2 == 0:
        for i in range(0, len(bilet)//2):
            s += int(bilet[i])
        for k in range(len(bilet)//2, len(bilet)):
            w += int(bilet[k])
    if s == w:
        print('счастливый билет')
        print(count)
        break
    count += 1
    s = 0
    w = 0

# 14
hint = input()
word = input()
zv = '*'*len(word)

print('\n'*25)
print(hint)
print(zv)

while answer != 1:
    answer = int(input('Буква или слово(0-буква, 1-слово)? '))

    if answer == 0:
        bukva = input()
        new_zv = list(zv)
        for i in range(len(word)):
            if word[i] == bukva:
                new_zv[i] = bukva
        zv = ''.join(new_zv)
        print(zv)

        if zv == word:
            print('Победа!')
            break

    elif answer == 1:
        slovo = input()
        if slovo == word:
            print('Победа!')
        else:
            print('Проигрыш!')
        break

# 15
secret = input("Введите четырёхзначное число с неповторяющимися цифрами: ")
while len(secret) != 4 or not secret.isdigit() or len(set(secret)) != 4:
    secret = input("Ошибка! Повторите ввод: ")

print('\n' * 25)
print("Игра началась! У вас 10 попыток.\n")

for i in range(10):
    guess = input(f"Попытка {i + 1}. Введите число: ")

    if len(guess) != 4 or not guess.isdigit():
        print("Введите корректное четырёхзначное число.")
        continue

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

# 17


def evaluate(expr):
    expr = expr.replace(" ", "")
    while '(' in expr:
        close_idx = expr.find(')')
        open_idx = expr.rfind('(', 0, close_idx)
        inner_expr = expr[open_idx + 1:close_idx]
        result = str(calc(inner_expr))
        expr = expr[:open_idx] + result + expr[close_idx + 1:]
    return calc(expr)


def calc(expr):
    nums = []
    num = ''
    sign = 1
    i = 0

    while i < len(expr):
        char = expr[i]
        if char == '+':
            nums.append(sign * float(num))
            num = ''
            sign = 1
        elif char == '-':
            nums.append(sign * float(num))
            num = ''
            sign = -1
        elif char in '*/':
            prev = sign * float(num)
            num = ''
            i += 1
            while i < len(expr) and expr[i] == ' ':
                i += 1
            next_num = ''
            while i < len(expr) and (expr[i].isdigit() or expr[i] == '.'):
                next_num += expr[i]
                i += 1
            i -= 1
            if char == '*':
                num = str(prev * float(next_num))
            else:
                num = str(prev / float(next_num))
            sign = 1
        else:
            num += char
        i += 1

    if num:
        nums.append(sign * float(num))

    return sum(nums)


expr = input("Введите арифметическое выражение: ")
try:
    result = evaluate(expr)
    print("Результат:", result)
except Exception as e:
    print("Ошибка в выражении:", e)

# 18


def justify(text, width):
    words = text.split()
    lines = []
    current_line = []

    current_len = 0
    for word in words:
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

    total_chars = sum(len(word) for word in words)
    spaces_needed = width - total_chars
    gaps = len(words) - 1
    space_between = spaces_needed // gaps
    extra_spaces = spaces_needed % gaps

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

# 19
dic = pyphen.Pyphen(lang='ru_RU')


def split_word(word, max_len):
    hyphenated = dic.inserted(word).split('-')
    result = []
    part = ''
    for syllable in hyphenated:
        if len(part + syllable) + 1 <= max_len:
            part += syllable
        else:
            if part:
                result.append(part + '-')
            part = syllable
    if part:
        result.append(part)
    return result


def justify(text, width):
    words = text.split()
    lines = []
    current_line = []
    current_len = 0

    for word in words:
        if len(word) > width:
            parts = split_word(word, width)
            for part in parts:
                if current_len + len(part) + len(current_line) <= width:
                    current_line.append(part)
                    current_len += len(part)
                else:
                    lines.append(align_line(current_line, width))
                    current_line = [part]
                    current_len = len(part)
            continue

        if current_len + len(word) + len(current_line) <= width:
            current_line.append(word)
            current_len += len(word)
        else:
            lines.append(align_line(current_line, width))
            current_line = [word]
            current_len = len(word)

    if current_line:
        lines.append(" ".join(current_line).ljust(width))

    return "\n".join(lines)


def align_line(words, width):
    if len(words) == 1:
        return words[0].ljust(width)

    total_chars = sum(len(w) for w in words)
    total_spaces = width - total_chars
    gaps = len(words) - 1

    space = total_spaces // gaps
    extra = total_spaces % gaps

    line = ''
    for i, word in enumerate(words[:-1]):
        line += word + ' ' * (space + (1 if i < extra else 0))
    line += words[-1]
    return line


text = input("Введите текст: ")
width = int(input("Введите ширину колонки: "))

formatted = justify(text, width)
print("\nОтформатированный текст:\n")
print(formatted)

# 20


def number_to_words(n):
    units = ["", "один", "два", "три", "четыре", "пять",
             "шесть", "семь", "восемь", "девять"]
    teens = ["десять", "одиннадцать", "двенадцать", "тринадцать",
             "четырнадцать", "пятнадцать", "шестнадцать",
             "семнадцать", "восемнадцать", "девятнадцать"]
    tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят",
            "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    hundreds = ["", "сто", "двести", "триста", "четыреста", "пятьсот",
                "шестьсот", "семьсот", "восемьсот", "девятьсот"]

    def group_to_words(n, gender='m'):
        words = []
        n = int(n)
        h = n // 100
        t = (n % 100) // 10
        u = n % 10

        words.append(hundreds[h])

        if t == 1:
            words.append(teens[u])
        else:
            words.append(tens[t])
            if gender == 'f':
                words.append(["", "одна", "две"][u]
                             if u in [1, 2] else units[u])
            else:
                words.append(units[u])

        return ' '.join(filter(None, words))

    def get_form(n, forms):
        if 11 <= n % 100 <= 14:
            return forms[2]
        elif n % 10 == 1:
            return forms[0]
        elif 2 <= n % 10 <= 4:
            return forms[1]
        else:
            return forms[2]

    if n == 0:
        return "ноль"

    parts = []
    millions = n // 1_000_000
    thousands = (n % 1_000_000) // 1_000
    rest = n % 1_000

    if millions:
        parts.append(group_to_words(millions))
        parts.append(get_form(millions, ["миллион", "миллиона", "миллионов"]))

    if thousands:
        parts.append(group_to_words(thousands, gender='f'))
        parts.append(get_form(thousands, ["тысяча", "тысячи", "тысяч"]))

    if rest:
        parts.append(group_to_words(rest))

    return ' '.join(parts)


num = int(input("Введите число (до 900000000): "))
if 1 <= num <= 900_000_000:
    print(number_to_words(num))
else:
    print("Число вне допустимого диапазона!")
