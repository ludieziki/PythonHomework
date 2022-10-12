#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#Пример:
#- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibonacci(n):
    if n in (1, 2):
        return 1
    if n == 0: return 0
    if n == -1: return 1
    if n < -1: return fibonacci(n + 2) - fibonacci(n + 1)
    return fibonacci(n - 1) + fibonacci(n - 2)
 
k = 8
fibonacci_list = [] 

for i in range(-k, k+1):
    fibonacci_list.append(fibonacci(i))

print(fibonacci_list)