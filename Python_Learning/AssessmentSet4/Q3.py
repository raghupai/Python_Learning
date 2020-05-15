'''
Created on 15-May-2020

@author: raghuveer
'''

def calculate(var1,var2):
    while(var1 != var2):
        if(var1 > var2):
            return calculate(var1-var2, var2)
        else:
            return calculate(var1, var2-var1)
    return var1

print(calculate(60,30))