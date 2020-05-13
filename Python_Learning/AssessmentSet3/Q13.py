'''
Created on 14-May-2020

@author: raghuveer
'''

try:
    try:
        list1 = [1, 0, 2, 4]
        var1, var2, var3 = list1
        var1/var2
    except ValueError:
        print("VE")
except ZeroDivisionError:
    print("ZD")
except:
    print("CA")
        