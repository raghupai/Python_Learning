'''
Created on 09-May-2020

@author: raghuveer
'''
def verify(num1,num2):
    if num1 > num2:
        return num1
    elif num1 == num2:
        return 1
    else:
        return num2

def display(arg1,arg2):
    if(verify(arg1,arg2)==arg1):
        print("A")
    elif(verify(arg1,arg2)==1):
        print("C")
    else:
        print("B")

display(1000,3500)