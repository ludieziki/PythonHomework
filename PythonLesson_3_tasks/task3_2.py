#Напишите программу, которая найдёт произведение пар чисел списка.
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

numbers = [2, 3, 4, 5, 6, 7]
multiply_by_pairs = []
for i in range(0, len(numbers)//2 + len(numbers)%2):
    #print(i, len(numbers)%2, len(numbers))
    multiply_by_pairs.append(numbers[i] * numbers[-i-1])

print(numbers, 'произведение пар элементов -> ', multiply_by_pairs)