'''
Created on 16-May-2020

An organization has decided to provide salary hike to its employees based on their job level. 
Employees can be in job levels 3 , 4 or 5. Hike percentage based on job levels are given below:

Job level - Hike Percentage (applicable on current salary)

3 - 15

4 - 7

5 - 5

In case of invalid job level, consider hike percentage to be 0.

Given the current salary and job level, write a Python program to find and display the new salary of an employee.

@author: raghuveer
'''

def Salary_Hike(job_level):
    hike = 0
    
    if (job_level == 3):
        hike = 15
    elif (job_level == 4):
        hike = 7
    elif (job_level == 5):
        hike = 5
    else:
        print("Incorrect Job Level")
        
    return hike

job_level = int(input("Enter your job level:"))

salary = int((input("Enter your salary: ")))

print("Your new salary is " + str(salary + (0.01 * salary * Salary_Hike(job_level))))