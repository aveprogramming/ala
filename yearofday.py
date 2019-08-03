from calendar import day_name
import calendar


day = input()
day_num = int()
year = 2019
month = 8

for i, n in enumerate(day_name):
    if n == day:
        day_num = i
        # print(day_num)

while True:
    if calendar.weekday(year, month, 1) == day_num:
        break
    month -= 1
    if month == 0:
        month = 12
        year -= 1


print(month, year)