def reverse(func):
    def wrapper(*args):
        print("Function's name - {}".format(func.__name__))
        print('Arguments-',*args)
        return func()
    return wrapper

@reverse
def result():
    print('This is the result of the second function')

result(123)