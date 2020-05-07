'''
Created on 07-May-2020

@author: raghuveer
'''

number_of_passengers=2
number_of_baggage=2
security_check=True
for passenger_count in range(1, number_of_passengers+1):
    baggage_count =1
    while (baggage_count<=number_of_baggage):
        if(security_check==True):
            print("Security check of passenger:", passenger_count, "-- baggage:", baggage_count,"baggage cleared")
        else:
            print("Security check of passenger:", passenger_count, "-- baggage:", baggage_count,"baggage not cleared")
        baggage_count+=1