# (g) Write a program that prints the next 20 leap years.

import datetime

year = datetime.datetime.now().year

count = 0 

print("next 20 Leap years:")

while count < 20:
    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year, " ", end= "")
        count += 1
    year += 1