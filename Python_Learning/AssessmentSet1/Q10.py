'''
Created on 11-May-2020

@author: raghuveer
'''

def find_sum(a,b):
    try:
        print(a+c)
    except ValueError:
        print("Function name error")
    finally:
        print("Sum finally")
try:
    find_sum(12,13)
except NameError:
    print("Invocation name error")
finally:
    print("Invocation finally")