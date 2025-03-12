# 1
import turtle as ttl
year = int(input())
if year // 4 == 0:
    print(366)
else:
    print(365)

# 2
xc = float(input('Координаты по Х окружности: '))
yc = float(input('Координаты по Y окружности: '))
r = float(input('Координаты по R окружности: '))
x = float(input('Координаты по Х точки: '))
y = float(input('Координаты по Y точки: '))

if (xc - x) ** 2 + (yc - y) ** 2 < r ** 2:
    print("Точка внутри окружности.")
else:
    print("Точка вне окружности.")

ttl.up()
ttl.setposition(xc, yc - r)
ttl.pendown()
ttl.circle(r)
ttl.up()
ttl.setposition(x, y)
ttl.down()
ttl.dot(10)
ttl.done()

# 3
number = int(input('Введите число: '))
a = number // 1000
b = (number // 100) % 10
c = (number // 10) % 10
d = number % 10
if a == d and b == c:
    print('настоящее')
else:
    print('кривое')

# 4
number = int(input('Введите число попугаев: '))
digit = number % 10
if digit == 1:
    print(f'{number} попугай')
elif digit > 1 and digit < 5:
    print(f'{number} попугая')
else:
    print(f'{number} попугаев')

# 5
weight = float(input())
height = float(input())
height = height*0.0254  # 1 дюйм = 0.0254м
weight = weight*0.4535923745  # 1 фунт = 0.4535923745 кг
BMI = weight/(height**2)
print(BMI)
if BMI < 16:
    print('Выраженный дефицит массы тела')
elif BMI >= 16 and BMI < 18.5:
    print('Недостаточная масса тела')
elif BMI >= 18.5 and BMI < 25:
    print('Норма')
elif BMI >= 25 and BMI < 30:
    print('Избыточная масса тела')
elif BMI >= 30 and BMI < 35:
    print('Ожирение первой степени')
elif BMI >= 35 and BMI < 40:
    print('Ожирение второй степени')
else:
    print('Ожирение третьей степени')

# 6
first_day = int(input())
second_day = int(input())
third_day = int(input())
count = 0

if first_day == second_day:
    count += 1
if first_day == third_day:
    count += 1
if second_day == third_day:
    count += 1
if count > 0 and count < 3:
    count += 1
print(count)

# 7
n = int(input('Кол-во станций на ветке: '))
k = int(input('Станция отправдения: '))
m = int(input('Станция назначения: '))

if abs(m - k) > n - abs(k - m):
    print(n - abs(k-m)-1)
else:
    print(abs(m-k)-1)

# 8
knat = int(input())
galleon = knat // (17*29)
sikl = (knat - galleon*17*29) // 29
rest = knat - galleon*17*29 - sikl*29
if galleon > 0:
    print(f'{galleon} галлеонов')
if sikl > 0:
    print(f'{sikl} сиклей')
if rest > 0:
    print(f'{rest} кнатов')

# 9
data = input('Введите высоты башен: ')
first_tower, second_tower, third_tower = map(int, data.split(' '))
a = max(first_tower, second_tower, third_tower)
c = min(first_tower, second_tower, third_tower)
if first_tower != a and first_tower != c:
    print(f'{a} {first_tower} {c}')
if second_tower != a and second_tower != c:
    print(f'{a} {second_tower} {c}')
if third_tower != a and third_tower != c:
    print(f'{a} {third_tower} {c}')

# 10
number = int(input('Введите PIN-код: '))
a = number // 1000
b = (number // 100) % 10
c = (number // 10) % 10
d = number % 10
long = len(str(number))
if number < 1900 or number > 2050:
    if long == 4:
        if a != b and a != c and a != d:
            if b != c and b != d:
                if c != d:
                    print('OK')
                else:
                    print('ERROR')
            else:
                print('ERROR')
        else:
            print('ERROR')
    else:
        print('ERROR')
else:
    print('ERROR')
