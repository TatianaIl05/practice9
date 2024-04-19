from math import sqrt
n = float(input())

while n <= 2:
    print('Неверное значение')
    n = float(input())

while n >= 2:
    n = sqrt(n)
    print(f'{n:.3f}')
