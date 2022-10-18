#Вычислить число c заданной точностью d
#Пример:
#- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import random

k = 1
s = 0

d = random.uniform(10**-1, 10**-10)

print('d =', d)

for i in range(100):

	# even index elements are positive
	if i % 2 == 0:
		s += 4/k
	else:

		# odd index elements are negative
		s -= 4/k

	# denominator is odd
	k += 2
	
print(s)
