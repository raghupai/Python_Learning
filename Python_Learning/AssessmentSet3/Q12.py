'''
Created on 13-May-2020

@author: raghuveer
'''

try:
    try:
        int(var1)
    except TypeError:
        print("TE1", end=" ")
    except NameError:
        print("NE1", end=" ")
    except ValueError:
        print("VE1", end=" ")
    var1='A'
    'Z'/0
except TypeError:
    print("TE2", end=" ")
except ZeroDivisionError:
    print("ZE2", end=" ")
        