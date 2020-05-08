'''
Created on 08-May-2020

@author: raghuveer
'''

def encode(message):
    str1 =""
    count = 0
    for i in range(1,len(message)): 
        if (message[i] == message[i-1]):
            count += 1
        else:
            str1 = str1+str(count)+message[i]
    
    return str1
        
    #Remove pass and write your logic here

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)