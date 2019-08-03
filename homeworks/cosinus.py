from math import factorial
from math import cos

x = int(input())
n = int(input())

a = x ** 2 / factorial(2)
b = 1 - a
elem = -1 * a

for i in range(x):
    result = b - a
    print(cos(result))



