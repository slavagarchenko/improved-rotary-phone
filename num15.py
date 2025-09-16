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
