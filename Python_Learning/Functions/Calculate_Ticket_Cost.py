'''
Created on 07-May-2020

@author: raghuveer
'''

def calculate_total_ticket_cost(no_of_adults, no_of_children):
    ticket_price = 37550.0
    service_tax = 7
    discount = 10
    
    temp = (no_of_adults * ticket_price) + (no_of_children * ticket_price / 3)
    
    total_ticket_cost = (temp + temp * (service_tax / 100)) * (1 - (discount / 100))

    return total_ticket_cost


#Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost=calculate_total_ticket_cost(3,1)
print("Total Ticket Cost:",total_ticket_cost)