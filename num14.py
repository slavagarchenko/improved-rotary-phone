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
