def number_to_words(n):
    units = ["", "один", "два", "три", "четыре",
             "пять", "шесть", "семь", "восемь", "девять"]
    teens = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать",
             "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят",
            "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    hundreds = ["", "сто", "двести", "триста", "четыреста",
                "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]

    def convert(num, is_female=False):
        hu = num // 100
        te = (num % 100) // 10
        un = num % 10
        result = []
        if hu > 0:
            result.append(hundreds[hu])
        if te == 1:
            result.append(teens[un])
        else:
            if te > 0:
                result.append(tens[te])
            if un > 0:
                if is_female and un in [1, 2]:
                    if un == 1:
                        result.append("одна")
                    else:
                        result.append("две")
                else:
                    result.append(units[un])
        return " ".join(result)

    def get_form(number, forms):
        if 11 <= number % 100 <= 14:
            return forms[2]
        elif number % 10 == 1:
            return forms[0]
        elif 2 <= number % 10 <= 4:
            return forms[1]
        else:
            return forms[2]

    if n == 0:
        return "ноль"

    millions = n // 1000000
    thousands = (n % 1000000) // 1000
    units_part = n % 1000
    parts = []

    if millions > 0:
        parts.append(convert(millions))
        parts.append(get_form(millions, ["миллион", "миллиона", "миллионов"]))

    if thousands > 0:
        parts.append(convert(thousands, True))
        parts.append(get_form(thousands, ["тысяча", "тысячи", "тысяч"]))

    if units_part > 0:
        parts.append(convert(units_part))

    return " ".join(parts)


num = int(input("Введите число (до 900000000): "))
if 0 <= num <= 900000000:
    print(number_to_words(num))
else:
    print("Число вне диапазона")
