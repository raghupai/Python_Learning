'''
Created on 14-May-2020

@author: raghuveer
'''

def func1():
    try:
        var1 = 1/0
        return 1
    except ZeroDivisionError:
        var1 = 1/0
        return 2
    finally:
        return 3

print(func1())