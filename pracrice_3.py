import math


#1
btc_rub = float(input())
print(round((btc_rub//100)%10))


#2
time=int(input())
hours=time//3600
min=(time-hours*3600)//60
sec=time-hours*3600-min*60
print(f'{hours} часов {min} минут {sec} секунд')


#3
number=int(input())
print(number%2)


#4
data = input()
x, y, n=map(int, data.split())
rub = x*n+(y*n)//100
kop = (y*n)%100
print(f'{rub} рублей {kop} копеек')


#5
n = int(input())
L_bracket=chr(ord('('))
R_bracket=chr(ord(')'))
R_slash=chr(92)
L_slash=chr(ord('/'))
underline=chr(ord('_'))
equal=chr(ord('='))
dot=chr(ord('.'))
quotes=chr(ord("'"))
Double_quotes=chr(ord('"'))
up = L_bracket + R_slash + 3*underline + L_slash + R_bracket + ' '
middle = L_bracket+equal + quotes + dot + quotes + equal + R_bracket + ' '
down = (L_bracket + Double_quotes + R_bracket + underline +
        L_bracket + Double_quotes + R_bracket + ' ')
print(f'{up*n}\n{middle*n}\n{down*n}')


#6
k = input()
n = int(input())
r = int(input())
sequence = int(k*n)
print(sequence*r)


#7
raw = input('enter number: ')
try:
    num = int(raw)
    print(num)
except ValueError:
    num = None
    print("Введено не число")


#8
data = input()
a, b, c=map(int, data.split())

if a + b > c and a + c > b and b + c > a:
    angle_a = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
    angle_b = math.acos((a**2 + c**2 - b**2) / (2 * a * c))
    angle_c = math.acos((a**2 + b**2 - c**2) / (2 * a * b))

    A_deg = math.degrees(angle_a)
    B_deg = math.degrees(angle_b)
    C_deg = math.degrees(angle_c)

    print(A_deg)
    print(B_deg)
    print(C_deg)
else:
    print("Такой треугольник не существует.")


#9
ATT = int(input()) # попытки прохождения
COMP = int(input()) # завершения
YDS = int(input()) # пробежки
TD = int(input()) # пасы на тачдаун
INT = int(input()) # перехваты
a = ((COMP / ATT) - 0.3) * 5
b = ((YDS / ATT)-3) * 0.25
c = (TD / ATT) * 20
d = 2.375 - ((INT / ATT) * 25)
passer_rating = (a + b + c + d) / 6 * 100
print(passer_rating)


#10
data = input()
x, y = map(int, data.split())
max_number = max(x, y)
min_number = min(x, y)
print(max_number%min_number+1)


#11
n = int(input())
hours = n//30
minutes = (n-hours*30)*2
print(f'{hours} часов {minutes} минут')


#12
from datetime import date
print(date.today())


#13
n = int(input()) #колво строк на странице
c = int(input()) #колво стобцов на странице
record_number = int(input())
records_per_page = c*n
page_number = (record_number-1)//records_per_page+1
record_on_page = (record_number-1)%records_per_page
column_number = (record_on_page//n)+1
string_number = (record_on_page%n)+1
print(f'страница {page_number}, стобец {column_number}, строка {string_number}')