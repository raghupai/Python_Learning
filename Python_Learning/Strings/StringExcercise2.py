'''
Created on 07-May-2020

@author: raghuveer
'''
def count_names(name_list):
    count1=0
    count2=0
    
    #start writing your code here
    #Populate the variables: count1 and count2
    for i in name_list:
        if (i.endswith("at") and not i.startswith("at")):
            count1 += 1
    
    for i in name_list:
        if (i.find("at") > 0 or i.startswith("at") ):
            count2 += 1
    

    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    print("_at -> ",count1)
    print("%at% -> ",count2)


#Provide different names in the list and test your program
name_list=["at","Cat","rabbit","matter"]
count_names(name_list)