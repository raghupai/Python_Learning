'''
Created on 15-May-2020

@author: raghuveer
'''

def fun(var1):
    if (var1 < 1):
        return 0
    elif (var1 % 2 == 0):
        return (fun(var1-1))
    else:
        return var1 + fun(var1-2)
    
print(fun(10))