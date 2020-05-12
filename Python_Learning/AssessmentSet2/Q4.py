'''
Created on 12-May-2020

@author: raghuveer
'''

ship_crew = {
    "Co-Captain" : "Jack",
    "Chief Officer" : "Mack",
    "Chief Steward" : "Harry",
    "Chief Cook" : "Mala"
    }

ship_crew['Captain']=ship_crew['Co-Captain']
ship_crew['Co-Captain']="Tom"

print(ship_crew)