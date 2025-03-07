#1
word = input()
if word == 'пароль':
    print('Проходите!')
else:
    print('Доступ запрещен')

#2
fisrt_word = input('Первое слово: ')
second_word = input('Второе слово: ')
words = fisrt_word + ' ' + second_word
if words == 'Генрих Герц':
    print('Верно')
else:
    print('Неверно')

#3
print('Как звали главного персонажа романов '
      'Яна Ялеминга о вымышленном шпионе '
      'секретной разведывательной службы Великобритании?')
name = input()
name  = name.lower()
if name == 'джеймс бонд' or name == 'агент 007':
    print('Верно')
else:
    print('Неверно')

#4
print('Вы поедете на бал?')
answer = input()
answer = answer.lower()
if answer == 'да' or answer == 'нет':
    print('Неверно')
else:
    print('Верно')

#5
first_quality = int(input('Поймал первый рыбак: '))
second_quality = int(input('Поймал второй рыбак: '))
if first_quality > second_quality:
    print(first_quality)
elif first_quality < second_quality:
    print(second_quality)
else:
    print('Одинаково')

#6
data = input('Введите счет: ')
first_score, second_score = map(int, data.split(':'))
if first_score > second_score:
    print(1)
elif first_score < second_score:
    print(2)
else:
    print(0)

#7
data = input('Введите счет: ')
kirill_score, arina_score, sergey_score = map(int, data.split(' '))
if kirill_score > arina_score and kirill_score > sergey_score:
    print(kirill_score)
elif kirill_score < arina_score and arina_score > sergey_score:
    print(arina_score)
elif kirill_score < sergey_score and sergey_score > arina_score:
    print(sergey_score)

#8
user_name = input('Здравствуйте! Как Вас зовут? ')
print(f'Очень приятно, {user_name}! Меня зовут Марк')
age = int(input('Сколько Вам лет? '))
if age > 78:
    print(f'Да, {user_name}, Вы старше меня на {age - 78} лет')
else:
    print(f'Да, {user_name}, Вы младше меня на {78 - age} лет')
opinion = input('Вам нравится программировать? ')
if opinion == 'да':
    print('Превосходно! Уверен, у Вас получится написать множество полезных и хороших программ.')
if opinion == 'нет':
    print('Жаль. Я думал, Вы сможете написать интересную программу для меня.')

#9
first_answer = input('Собака короткошерстной породы? ')
if first_answer == 'да':
    second_answer = input('Рост собаки менее 50см? ')
    if second_answer == 'да':
        third_answer = input('У собаки короткий хвост? ')
        if third_answer == 'да':
            print('Английский бульдог')
        else:
            forth_answer = input ('У собаки длинные уши? ')
            if forth_answer == 'да':
                print('Гончая')
            else:
                fifth_answer = input('У собаки короткое тело? ')
                if fifth_answer == 'да':
                    print('Мопс')
                else:
                    print('Чихуахуа')
    else:
        third_answer = input('Собака весит больше 50 кг? ')
        if third_answer == 'да':
            print('Датский дог')
        else:
            print('Фоксхаунд')
else:
    second_answer = input('Рост собаки менее 50см? ')
    if second_answer == 'да':
        third_answer = input('У собаки доброжелательный характер? ')
        if third_answer == 'да':
            print('Кокер-спаниэль')
        else:
            print('Ирландский сеттер')
    else:
        third_answer = input('У собаки рост меньше 70см? ')
        if third_answer == 'да':
            forth_answer = input('У собаки длинные уши? ')
            if forth_answer == 'да':
                print('Большой вандейский грифон')
            else:
                print('Колли')
        else:
            forth_answer = input('Окрас рыжий с белыми отметинами? ')
            if forth_answer == 'да':
                print('Сенбернар')
            else:
                fifth_answer = input('Белоснежный окрас? ')
                if fifth_answer == 'да':
                    print('Ирландский волкодав')
                else:
                    print('Ньюфаундленд')

#10
num_gears = int(input())
if num_gears % 2 == 0:
    print('да')
else:
    print('нет')
