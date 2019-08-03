def nuli(n):
    list = []
    for i in range(n):
        number = int(input())
        if number == 0:
            list.insert(0, number)
        else:
            list.append(number)
    return list

print(nuli(3))