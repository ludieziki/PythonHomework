# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11
x = input('Введите вещественное число ->   ')
# print(type(x))


def sumDigits(y):
    z = 0
    for i in range(len(y)):
        if y[i] == "." or y[i] == "," or y[i] == "-":
            y[i]
        else:
            z = z + int(y[i])

    return z


print(sumDigits(x))
