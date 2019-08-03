import random
from functools import reduce

n = int(input())

nums = []
for i in range(n):
    number = random.randrange(1, 10)
    nums.append(number)
print(nums)


reducer, mapper, predicate = input().split(' ')

mappers = {'negated': lambda x: -x,
           'inverted': lambda x: 1/x,
           'squared': lambda x: x*x}


filters = {'evens': lambda x: x % 2 == 0,
           'odds': lambda x: x % 2 != 0,
           'simples': lambda x: x in [1, 2, 3, 5, 7]}


f1 = list(filter(filters[predicate], nums))
f2 = list(map(mappers[mapper], f1))

nums = f2
s = set()
num = []

def reverse(*args):
    for item in nums:
        num.insert(0, item)
    return nums


def union(*args):
    for item in nums:
        s.add(item)
    return s


def join(*args):
    un = ' '
    for item in nums:
        un += str(item)
    return un


reducers = {'sum': reduce(lambda x, y: x+y, nums),
            'multiply': reduce(lambda x, y: x*y, nums),
            'join':reduce(join, nums),
            'union': reduce(union, nums),
            'reverse': reduce(reverse, nums)}

f3 = reducers[reducer]
print(f3)






