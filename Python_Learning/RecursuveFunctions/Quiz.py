'''
Created on 13-May-2020

@author: raghuveer
'''

def fun(number):
    if(number<2):
        return 1
    elif(number/2==2):
        return fun(number-1)
    else:
        return (number-1)*fun(number-1)

print(fun(7))