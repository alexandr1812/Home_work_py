# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4

# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5

# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]
 

from random import sample


def create_list(n):
    while n <= 0:
        print('Enter a positive value')
        n = int(input('Try again: '))
    arr = sample(range(1, n * 2), k=n)
    print(arr)
    return arr

genereted_list = create_list(int(input()))

def multiplication(arr):
    array = []
    revers_arr = arr[::-1]
    for i in range(len(arr) // 2 + len(arr) % 2):
        result = revers_arr[i] * arr[i]
        if i == len(arr) // 2:
            array.append(arr[i])
            break
        array.append(result)
    return array

print(multiplication(genereted_list))


