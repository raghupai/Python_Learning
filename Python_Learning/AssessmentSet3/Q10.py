'''
Created on 13-May-2020

@author: raghuveer
'''

try:
    list1 = [8, 4, 2, 0]
    value = len(list1[:-1])
    result = list1[0]/list1[value]
    print(result)
except IndexError:
    print("Index")
except ZeroDivisionError:
    print("Zero Division")
except:
    print("Catch All")