def reverse(func):
    def wrapper(*args):
        return func(*args[::-1])
    return wrapper

@reverse
def order(*args):
    return args


print(order(1,2,3,4,5))

