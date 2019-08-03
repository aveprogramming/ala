from math import acos,degrees

a = int(input())
b = int(input())
c = int(input())
if a + b > c:
    print('существует, сейчас найдем углы')
    angle1 = round(degrees(acos((a * a + b * b - c * c) / (2.0 * a * b))))
    angle2 = round(degrees(acos((a * a + c * c - b * b) / (2.0 * a * c))))
    angle3 = 180 - (angle1 + angle2)

    print(angle1, angle2, angle3)
else:
    print('не существует')


