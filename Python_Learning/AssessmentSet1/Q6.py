'''
Created on 11-May-2020

@author: raghuveer
'''

def value(num1):
    list1=[]
    while num1!=0:
        if num1%2==0:
            list1.append(num1)
        else:
            break
        num1-=2
    print(list1)
value(10)