'''
Created on 15-May-2020

@author: raghuveer
'''

def func1():
    try:
        1/0
        return 1
    except ZeroDivisionError:
        "ABC"+1
        return 2
    finally:
        int('A')
        return 3

try:
    result=func1()
    print(result)
except:
    print(4)