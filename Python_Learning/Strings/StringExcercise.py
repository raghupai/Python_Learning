'''
Created on 07-May-2020

@author: raghuveer
'''
def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    temp = 101
    #Write your logic here
    for i in range(0,no_of_passengers):
        ticket_number_list.append(airline+":"+source[0:3]+":"+destination[0:3]+":"+str(temp + i))
    
    if (no_of_passengers > 5):
        ticket_number_list = ticket_number_list[-5:]
    
    #Use the below return statement wherever applicable
    return ticket_number_list

#Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("AI","Bangalore","London",7))