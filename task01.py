# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5

# out
# [10, 2, 3, 8, 9]
# 22

# in
# 4

# out
# [4, 2, 4, 9]
# 8


from random import sample


def find_number_odd_pos(number):
    sum = 0
    array = sample(range(1, number * 2), k=number)
    print(array)
    for i in range(0, len(array), 2):
        sum += array[i]
    return sum


print(find_number_odd_pos(int(input('Enter the namber: '))))
