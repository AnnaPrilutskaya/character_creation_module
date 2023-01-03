from math import sqrt
import itertools


message = (f'Добро пожаловать в самую лучшую программу для вычисления ' 
           f'квадратного корня из заданного числа')
print (message)


def CalculateSquareRoot(Number):
    """ Вычисляет квадратный корень."""
    return sqrt(Number)

    
def Calc(your_number) :
    if your_number<=0:
        return root = 0
    print(f'Мы вычислили квадратный корень'
          f'из введённого вами числа.'
          f'Это будет: {CalculateSquareRoot(your_number)}')


print(message)
Calc (25.5)