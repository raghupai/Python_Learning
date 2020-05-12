'''
Created on 12-May-2020

@author: raghuveer
'''

var = 200

if (var > 200):
    print("Within First Block")
    if (var == 150):
        print("Which is 150")
    elif (var == 100):
        print("which is 100")
elif (var > 50):
    print("Within Second Block")
    if (var % 5 == 0):
        print("Which is a multiple of 5")
    elif (var % 10 == 0):
        print("Which is a multiple of 10")
    else:
        print("Which is neither multiple of 5 nor multiple of 10")
else:
    print("Could not find true expression")
    
print("Good Bye!")