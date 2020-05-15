'''
Created on 15-May-2020

@author: raghuveer
'''

try:
    tupl1 = ([1,2], [3,4])
    list1 = [(1,2), (3,4)]
    list2 = tupl1[0]
    list2[0] = 5
    list1[1] = (6,7)
    print(tupl1, list1)
except TypeError:
    print("ERR")