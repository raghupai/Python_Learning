'''
Created on 15-May-2020

@author: raghuveer
'''

var1, var2 = 10, 40

def func(var1):
    global var2
    var1, var2 = 20, 50
    print(var1, end=" ")
    print(var2, end=" ")
    
func(30)
print(var1, end=" ")
print(var2, end=" ")