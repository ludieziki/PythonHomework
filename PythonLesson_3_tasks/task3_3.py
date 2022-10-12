#Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#Пример:
#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

numbers = [1.1, 1.2, 3.1, 5, 10.01]

min_fraction = numbers[0]%1
max_fraction = numbers[0]%1

print(min_fraction)

for i in numbers:
    if i%1 > max_fraction: max_fraction = i%1
    if i%1 < min_fraction: min_fraction = i%1

print(max_fraction - min_fraction)
     