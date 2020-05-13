'''
Created on 13-May-2020

@author: raghuveer
'''

def divide(num1, num2):
    try:
        num3 = num1 / num2
        print(num3)
    except:
        print("Inside function")
try:
    divide(100, 0)
except:
    print("Outside function")