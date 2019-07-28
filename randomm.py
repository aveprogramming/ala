import random

number = random.randrange(1, 11)
usernumber = int(input())
while usernumber:
    if usernumber != number:
        print('Try more')
        usernumber = int(input())
    else:
        print('You guessed it!')
        break