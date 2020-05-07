'''
Created on 07-May-2020

@author: raghuveer
'''

baggage_count=100
no_of_baggage_picked = (int)(input ("Number of baggage:"))
while(baggage_count>0):
    baggage_count = baggage_count - no_of_baggage_picked
    print("No. of baggage remaining:",baggage_count)