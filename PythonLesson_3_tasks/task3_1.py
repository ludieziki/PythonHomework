#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример:
#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

numbers = [2, 3, 5, 9, 3]
sum_odd_numbers = 0
for i in range(1, len(numbers), 2):
    sum_odd_numbers = sum_odd_numbers + numbers[i]
    #print('i =', i, 'numbers = ', numbers[i])
    
print(numbers, 'сумма элементов списка, стоящих на нечётной позиции', sum_odd_numbers)