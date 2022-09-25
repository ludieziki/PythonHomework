# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
from tarfile import LENGTH_PREFIX


x = input('Введите X')
y = input('Введите Y')
z = input('Введите Z')
left = not(x or y or z)
r = not x and not y and not z
res = (left==r)
print(res)