'''
Created on 15-May-2020

@author: raghuveer
'''

def func(var1, var2, var3):
    if(var1 > var2):
        return("1")
    elif(var2 > var3):
        if(var1 > var3):
            return("2")
        else:
            return("3")
    else:
        return("4")
    
print(func(3, 5, 1))