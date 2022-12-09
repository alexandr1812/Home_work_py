# 4.* Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36

import random


def create_float_list(n):
    while n <= 0:
        print('Enter a positive value')
        n = int(input('Try again: '))
    array = [round(random.uniform(n, n*10), 2) for i in range(n)]
    return array


list_float = create_float_list(int(input()))
print(list_float)


def coverting_list(int_list):
    int_list = [int(i) for i in int_list]
    new_float_list = [float(i) for i in int_list]
    return new_float_list


new_list = coverting_list(list_float)


def find_difference(first_list, second_list):
    result = [round(i - j, 2) for i, j in zip(second_list, first_list)]
    max_min = max(result) - min(result)
    print(f"max = {max(result)}\nmin = {min(result)}")
    return round(max_min, 2)


result = find_difference(new_list, list_float)
print(f"Difference = {result}")
