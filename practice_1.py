#1
print("Hello, Python!")
#2
print("Привет, Python\nHello, Python\nBonjour, Python\n"
      "Hej, Python\nHola, Python")
#3
print('Привет, ', end=' ')
print('Python')
#4
L_bracket=chr(ord('('))
R_bracket=chr(ord(')'))
R_slash=chr(92)
L_slash=chr(ord('/'))
underline=chr(ord('_'))
equal=chr(ord('='))
dot=chr(ord('.'))
quotes=chr(ord("'"))
Double_quotes=chr(ord('"'))
print(f'{L_bracket}{R_slash}{3*underline}{L_slash}{R_bracket}'
      f'\n{L_bracket}{equal}{quotes}{dot}{quotes}{equal}{R_bracket}'
       f'\n{L_bracket}{Double_quotes}{R_bracket}{underline}'
       f'{L_bracket}{Double_quotes}{R_bracket}')
#5
print("Привет,Python\nHello, Python\nBonjour, Python\n"
      "Hej, Python\nHola, Python")
#6
user_name = input('Как Вас зовут? ')
print(f'Здравствуйте, {user_name}')
#7
user_name = input('Как Вас зовут? ')
print(f'Здравствуйте, {user_name}')
hobby = input('Что Вам нравится? ')
print(f'Отлично! {hobby} - это хорошее увлечение')
#8
login = input('Login: ')
old_password = input('Password: ')
new_password = input('New password: ')
print(f'User {login} has changed the password to {new_password}')
#9
print('Введите плей-лист папы:')
hit1 = input()
hit2 = input()
hit3 = input()
hit4 = input()
hit5 = input()
print(f'Плей-лист мамы:\n{hit5}\n{hit4}\n{hit3}\n{hit2}\n{hit1}')
#10
flight_number = input('номер рейса: ')
airline_name_rus = input('название авиакомпании (на русском языке): ')
airline_name_eng= input('название авиакомпании (на английском языке): ')
city_of_arrival_rus = input('город прилета (на русском языке): ')
city_of_arrival_eng = input('город прилета (на английском языке): ')
print(f'Заканчивается посадка на рейс {flight_number} '
      f'авиакомпании {airline_name_rus} до {city_of_arrival_rus}\n'
      f'This is final boarding call for {airline_name_eng} '
      f'flight {flight_number} to {city_of_arrival_eng}')
#11
user_name = input('Как Вас зовут? ')
print(f'Привет, {user_name}!')
#12
silver_watches = 96
silver_watch_price = 48
gold_watches = silver_watches // 16
total_cost = int(input('Введите общую стоимость чаосв: '))
silver_watch_cost = silver_watches * silver_watch_price
gold_watch_cost = total_cost - silver_watch_cost
if gold_watches > 0:
    gold_watch_price = gold_watch_cost / gold_watches
else:
    gold_watch_price = 0
print(gold_watch_price)
#13
blind_spot_R = float(input())
reception_range_R = float(input())
if reception_range_R < blind_spot_R:
    reception_range_R, blind_spot_R = blind_spot_R, reception_range_R
reception_range_S = 3.14*reception_range_R**2
blind_spot_S = 3.14*blind_spot_R**2
coverage_S = reception_range_S-blind_spot_S
print(coverage_S)
#14
result = int(input())
print(result-4)
#15
sm = float(input())
inch = 2.54*sm
foot = 12*inch
yard = 3*foot
mile = 1760*yard
print(f'{yard} ярдов\n{mile} мили\n{foot} футов\n{inch} дюймов')
