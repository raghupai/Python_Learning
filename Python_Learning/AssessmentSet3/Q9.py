'''
Created on 13-May-2020

@author: raghuveer
'''

elements = [2, 5, 6, 0]

try:
    div = elements[4]/elements[3]
except ZeroDivisionError:
    print("Infinity")
except IndexError:
    print("Index Error")
except Exception:
    print("0")
finally:
    print("In finally block")