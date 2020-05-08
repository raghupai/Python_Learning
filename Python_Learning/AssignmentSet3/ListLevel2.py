'''
Created on 08-May-2020
ARS Gems Store sells different varieties of gems to its customers.

Write a Python program to calculate the bill amount to be paid by a customer based on the list of gems and quantity purchased. Any purchase with a total bill amount above Rs.30000 is entitled for 5% discount. If any gem required by the customer is not available in the store, then consider total bill amount to be -1.

Assume that quantity required by the customer for any gem will always be greater than 0.

Perform case-sensitive comparison wherever applicable.

@author: raghuveer
'''

#lex_auth_012693795044450304151

def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    count = 0
    #Write your logic here
    
    for i in range(0,len(reqd_gems)):
        for j in range(0,len(gems_list)):
            if (reqd_gems[i].upper() == gems_list[j].upper()):
                bill_amount += reqd_quantity[i] * price_list[j]
                count +=1
            
    


        
    if (count != len(reqd_gems)):
        bill_amount = -1
    elif (bill_amount > 30000):
        bill_amount *= 0.95
    
        
    return bill_amount

#List of gems available in the store
gems_list=['Moonstone', 'Sapphire', 'Quartz']

#Price of gems available in the store. gems_list and price_list have one-to-one correspondence
price_list=[3498, 1257, 5467]

#List of gems required by the customer
reqd_gems=['quartz']

#Quantity of gems required by the customer. reqd_gems and reqd_quantity have one-to-one correspondence
reqd_quantity=[5, 8]

bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)