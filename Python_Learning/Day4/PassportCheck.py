'''
Created on 07-May-2020

@author: raghuveer
'''

passport_status="valid"
ticket_status="Confirmed"
luggage_weight=32
weight_limit=30  #Weight limit for the airline
extra_luggage_charge=0
if(passport_status=="valid"):
    print("Airport security cleared")
    if(ticket_status=="Confirmed"):
        if(luggage_weight>0 and luggage_weight<=weight_limit):
            print("Check-in cleared")
        else:
            extra_luggage_charge=300*(luggage_weight-weight_limit)
            if(extra_luggage_charge>0):
                print("Extra luggage charge is Rs.", extra_luggage_charge)
                print("Please make the payment to clear check-in")
            else:
                print("Sorry, ticket is not confirmed")
else:
    print("Invalid passport")