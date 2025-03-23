# 1
R = 6.5
a = float(input('Длина покрытия: '))
b = float(input('Ширина покрытия: '))

if 0.5*a ** 2 + 0.5*b ** 2 <= R**2:
    print("да")
else:
    print("нет")

# 2
data_okno = input('Введите размеры окна: ')
data_kirpich = input('Введити размеры кирпича: ')
a, b = map(int, data_okno.split('x'))
c, d, e = map(int, data_kirpich.split('x'))
if min(c, d, e) <= a:
    if (c+d+e-min(c, d, e)-max(c, d, e)) < b:
        print('да')
elif min(c, d, e) <= b:
    if (c+d+e-min(c, d, e)-max(c, d, e)) < a:
        print('да')
    else:
        print('нет')
else:
    print('нет')

# 3
data_rayon = input('Введите размеры района: ')
k = int(input('Кол-во кварталов: '))
n, m = map(int, data_rayon.split('x'))
count = 0
if k < m*n:
    for row in range(1, n):  # Перекрываем горизонтальную улицу
        if (row * m) >= k and ((n - row) * m) >= (n * m - k):
            count += 1
    for col in range(1, m):
        if (col * n) >= k and ((m - col) * n) >= (n * m - k):
            count += 1
else:
    print('некорректный ввод')
if count > 0:
    print('успешно')
else:
    print('неосуществимо')

# 4
data = input()
digit = int(data[1])
if digit % 2 == 1:
    if (data[0] == 'a' or data[0] == 'c' or data[0] == 'e' or data[0] == 'g'):
        print('черная клетка')
    else:
        print('белая клетка')
else:
    if (data[0] == 'a' or data[0] == 'c' or data[0] == 'e' or data[0] == 'g'):
        print('белая клетка')
    else:
        print('черная клетка')

# 5
bukvi = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
data = input('введите ход: ')
start, end = data.split('-')
print(start, end)
for i in range(8):
    if start[0] == bukvi[i]:
        if bukvi[i-1] == end[0] or bukvi[i+1] == end[0]:
            if int(start[1]) + 2 == int(end[1]) or int(start[1]) - 2 == int(end[1]):
                print('верно')
            else:
                print('ошибка')
        elif bukvi[i-2] == end[0] or bukvi[i+2] == end[0]:
            if int(start[1]) + 1 == int(end[1]) or int(start[1]) - 1 == int(end[1]):
                print('верно')
            else:
                print('ошибка')

# 6
data = input('Введите данные: ')
n, k, m = map(int, data.split(' '))
odin_krug = (n + k - 1) // k
total_time = odin_krug * 2 * m
print(total_time)

# 7
data = int(input('Кол-во суш которые вы хотите заказать: '))
sushi = data
count = 0
for i in range(data):
    if sushi % 5 == 0 and sushi > 4:
        count += 1
    else:
        sushi -= 7
sushi = data
for k in range(data):
    if sushi % 7 == 0 and sushi > 6:
        count += 1
    else:
        sushi -= 5
if count > 0:
    print('да')
else:
    print('нет')

# 8
position = int(input('Введите порядковый номер цифры: '))
current_position = 1
if position == current_position:
    print(0)
current_position += 1
for number in range(1, 201):
    temp_number = number
    while temp_number > 0:
        digit = temp_number % 10
        temp_number //= 10
        if current_position == position:
            print(digit)
        current_position += 1

# 9
x_first = float(input('Координаты по Х второй окружности: '))
y_first = float(input('Координаты по Y второй окружности: '))
r_first = float(input('Координаты по R второй окружности: '))
x_second = float(input('Координаты по Х второй точки: '))
y_second = float(input('Координаты по Y второй точки: '))
r_second = float(input('Координаты по R второй окружности: '))

distance = ((x_second - x_first) ** 2 + (y_second - y_first) ** 2)**0.5
if distance > r_first + r_second:
    print('Окружности лежат одна вне другой, не касаясь')
elif distance < abs(r_first - r_second):
    print('Одна окружность лежит внутри другой, не касаясь')
elif distance == r_first + r_second:
    print('Окружности имеют внешнее касание')
elif distance == abs(r_first - r_second):
    print('Окружности имеют внутреннее касание')
else:
    print('Окружности пересекаются')

# 10
data_U_L_first = input(
    'Введите координаты верхней левой координаты первого прямоугольника: ')
data_D_R_first = input(
    'Введите координаты нижней правой координаты первого прямоугольника: ')
data_U_L_second = input(
    'Введите координаты верхней левой координаты второго прямоугольника: ')
data_D_R_second = input(
    'Введите координаты нижней правой координаты второго прямоугольника: ')
x1_l, y1_u = map(float, data_U_L_first.split(';'))
x1_r, y1_d = map(float, data_D_R_first.split(';'))
x2_l, y2_u = map(float, data_U_L_second.split(';'))
x2_r, y2_d = map(float, data_D_R_second.split(';'))
if x1_r < x2_l or x2_r < x1_l or y1_u < y2_d or y2_u < y1_d:
    print("Прямоугольники лежат вне друг друга, не касаясь")
elif (x1_r == x2_l or x1_l == x2_r) and (y1_d < y2_u and y1_u > y2_d):
    print("Прямоугольники имеют касание")
elif (y1_u == y2_d or y1_d == y2_u) and (x1_l < x2_r and x1_r > x2_l):
    print("Прямоугольники имеют касание")
elif (x1_l > x2_l and x1_r < x2_r and y1_d > y2_d and y1_u < y2_u):
    print("Первый прямоугольник полностью внутри второго, не касаясь")
elif (x2_l > x1_l and x2_r < x1_r and y2_d > y1_d and y2_u < y1_u):
    print("Второй прямоугольник полностью внутри первого, не касаясь")
else:
    print("Прямоугольники имеют пересечение")
