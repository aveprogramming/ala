# можно по половине строки смотреть len//2

def palindrom(x):
    x = list(x)
    if x == x[::-1]:
        return 'palindrom'
    else:
        return 'usual string'

print(palindrom('шалаш'))