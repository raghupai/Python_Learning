'''
Created on 10-May-2020

Write a Python program to check whether the given year is leap year or not.

@author: raghuveer
'''

def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False
    
num = int(input("Enter a year : "))

if (leap_year(num)):
    print(num, "is a leap year")
else:
    print(num, "is not a leap year")