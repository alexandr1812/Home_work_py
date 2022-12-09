# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000

# in
# 11
# out
# 1011

def converting(n):
    list_num = []
    while n > 0:
        remainder = n % 2
        int_division = n // 2
        n = int_division
        list_num.append((remainder))
    return "".join(map(str, list_num[::-1]))


print(converting(int(input())))

