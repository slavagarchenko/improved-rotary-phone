920

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
from datetime import datetime
now = datetime.now()
formatted_string = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_string)


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