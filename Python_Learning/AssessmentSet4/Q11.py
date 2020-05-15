'''
Created on 15-May-2020

@author: raghuveer
'''

def func(var1=1, var2=2):
    print(var1, end=" ")
    print(var2, end=" ")
    
func(100,None)
func(var2=20, var1=10)
func(var2=10)