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
