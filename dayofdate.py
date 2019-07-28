import calendar
date = input()
date = date.split('.')
date = calendar.weekday(int(date[-1]), int(date[-2]), int(date[-3]))
day = calendar.weekheader(3).split(' ')
print(day[date])





