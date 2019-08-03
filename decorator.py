def reverse(func):
    def wrapper(*args):
        return func(*args[::-1])
    return wrapper

print(reverse((1,2,3)))