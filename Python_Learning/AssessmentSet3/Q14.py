'''
Created on 14-May-2020

@author: raghuveer
'''

try:
    list1 = ["ABC", "PQR", "XYZ", "GHIJKL"]
    str = ""
    for value in list1:
        str += str(value)
    value = len(str) / len(str) % 3
except TypeError:
    print("TE")
except ValueError:
    print("VE")
except ZeroDivisionError:
    print("ZD")
except:
    print("CA")