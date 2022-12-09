# 5. ** Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Негафибоначчи

# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21

# in
# 5
# out
# 5 -3 2 -1 1 0 1 1 2 3 5

def fib(num):
    a, b = 1, 1
    array = [0]

    for i in range(num):
        array.append(a)
        array.insert(0, a * (-1) ** 1)
        a, b = b, b + a
    
    return array

print(fib(int(input())))