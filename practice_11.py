# 1
import os
with open('input.txt', 'r', encoding='utf-8') as infile:
    data = infile.read()
upper_data = data.upper()
with open('output.txt', 'w', encoding='utf-8') as outfile:
    outfile.write(upper_data)

# 2
with open('input.txt', 'r', encoding='utf-8') as infile:
    lines = infile.readlines()
filtered_lines = [line for line in lines if line.lstrip().startswith('A')]

with open('output.txt', 'w', encoding='utf-8') as outfile:
    outfile.writelines(filtered_lines)

# 3
with open('input.txt', 'r', encoding='utf-8') as infile:
    lines = infile.readlines()
first_chars = [line[0] for line in lines if line]

result_word = ''.join(first_chars)

with open('output.txt', 'w', encoding='utf-8') as outfile:
    outfile.write(result_word)

# 4
with open('input.txt', 'r', encoding='utf-8') as infile:
    lines = infile.readlines()

long_lines = [line for line in lines if len(line.rstrip('\n')) > 20]
with open('output.txt', 'w', encoding='utf-8') as outfile:
    outfile.writelines(long_lines)

# 5
try:
    with open('input.txt', 'r', encoding='utf-8') as infile:
        numbers = infile.read().split()
        if len(numbers) != 3:
            raise ValueError("В файле должно быть ровно три числа.")
        a, b, c = map(int, numbers)
    result = a / b + c
    with open('output.txt', 'w', encoding='utf-8') as outfile:
        outfile.write(str(result))

except ValueError:
    with open('output.txt', 'w', encoding='utf-8') as outfile:
        outfile.write("data error")
except ZeroDivisionError:
    with open('output.txt', 'w', encoding='utf-8') as outfile:
        outfile.write("division by 0")

# 6
# solution.py

try:
    with open('input.txt', 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    if not lines:
        result = 'ERROR'
    else:
        try:
            N = int(lines[0].strip())
        except ValueError:
            result = 'ERROR'
        else:
            data_lines = lines[1:]

            if len(data_lines) == N:
                result = 'YES'
            else:
                result = 'NO'
except Exception:
    result = 'ERROR'

with open('output.txt', 'w', encoding='utf-8') as outfile:
    outfile.write(result)

# 7
with open('input.txt', 'r', encoding='utf-8') as infile:
    lines = infile.readlines()
filtered_lines = [line for line in lines if line.strip() != '100']
with open('input.txt', 'w', encoding='utf-8') as outfile:
    outfile.writelines(filtered_lines)
    outfile.writelines(filtered_lines)

# 8
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

with open('input.txt', 'r', encoding='utf-8') as infile:
    steps = list(map(int, infile.read().split()))
if len(steps) != 365:
    raise ValueError("Некорректное количество данных")
start_index = 0
results = []

for month_days in days_in_month:
    month_steps = steps[start_index:start_index + month_days]
    average = sum(month_steps) / month_days
    results.append(average)
    start_index += month_days
with open('output.txt', 'w', encoding='utf-8') as outfile:
    for avg in results:
        outfile.write(f"{avg}\n")

# 9
input_path = 'input.txt'
output_dir = 'simple'
output_path = os.path.join(output_dir, 'output.txt')
os.makedirs(output_dir, exist_ok=True)

with open(input_path, 'r', encoding='utf-8') as infile:
    lines = infile.readlines()
even_lines = [line for idx, line in enumerate(lines, start=1) if idx % 2 == 0]

with open(output_path, 'w', encoding='utf-8') as outfile:
    outfile.writelines(even_lines)

# 10


def date_to_day(day_str, month_str):
    day = int(day_str)
    month = int(month_str)
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = sum(days_in_month[:month - 1]) + day
    return total_days


with open('input.txt', 'r', encoding='utf-8') as infile:
    current_date = infile.readline().strip()
    N = int(infile.readline().strip())
    records = infile.readlines()
current_day_str, current_month_str = current_date.split('.')
current_day_num = date_to_day(current_day_str, current_month_str)
cell_storage = {}
for line in records:
    line = line.strip()
    cell_num_str, date_str = line.split()
    day_str, month_str = date_str.split('.')
    day_num = date_to_day(day_str, month_str)
    cell_num = int(cell_num_str)
    cell_storage[cell_num] = day_num
result_cells = []
for cell_num, start_day in cell_storage.items():
    duration = current_day_num - start_day
    if duration > 3:
        result_cells.append(cell_num)
result_cells.sort()
with open('output.txt', 'w', encoding='utf-8') as outfile:
    for cell in result_cells:
        outfile.write(f"{cell}\n")
