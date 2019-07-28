# x = int(input())
# y = int(input())
# z = x/y
# print(z)



# while True:
#     try:    #если блок отработал полностью, то попадаем в else i break
#         x = int(input())
#     except: # eсли исключение произошло, елсе не будет выполняться
#         print('error')
#     else:
#         break

#то же самое, только с циклом фор

# x = iter(range(3))
# for i in x:
#     print(i)
# for i in x:
#     print(i)
#
# x = {1:'a', 1.0:'b', True:'c'}
# print(x)

# s = input()
# d,m,y = map(int,s.split('.'))
# print(d,m,y)

n = 6
x = [i*i for i in range(n) if i%2]
print(x)