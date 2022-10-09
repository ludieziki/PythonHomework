# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

def is_int(number):
    return number.isdigit()

number = None

while not is_int(str(number)):
    number = input("Введите число N -> ")

number = int(number)

y = list(range(-number, number+1))

posToMultiply = open('file.txt')

mult = 1

for line in posToMultiply:
    #print(line)
    #print('Элемент', line, 'равен -> ', y[int(line)-1])
    if int(line) > len(y)-1:
        None
    else:
        mult = mult * y[int(line)-1]

print('Массив', y, 'сумма произведений на заданных позициях', mult)