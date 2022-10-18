#Вычислить число c заданной точностью d
#Пример:
#- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from math import acos
 
# Function that prints the
# value of pi upto N
# decimal places
def printValueOfPi():
 
    # Find value of pi upto 3 places
    # using acos() function
    pi = round(2 * acos(0.0), 3)
 
    # Print value of pi upto
    # N decimal places
    print(pi)

if __name__ == "__main__":
    printValueOfPi