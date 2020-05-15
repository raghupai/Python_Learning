'''
Created on 10-May-2020

Write a python program that displays a message as follows for a given number:

If it is a multiple of three, display "Zip"

If it is a multiple of five, display "Zap".

If it is a multiple of both three and five, display "Zoom".

If it does not satisfy any of the above given conditions, display "Invalid".

@author: raghuveer
'''
from pip._vendor.distlib.compat import raw_input

num = raw_input("Enter a number: ")

num = int(num)
if (num % 3 == 0 and num % 5 == 0):
    print("Zoom")
elif (num % 3 == 0):
    print("Zip")
elif(num % 5 == 0):
    print("Zap")
else:
    print("Invalid")