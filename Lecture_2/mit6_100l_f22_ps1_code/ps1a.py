## 6.100A PSet 1: Part A
## Name:
## Time Spent:
## Collaborators:

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent you wanna save every month:"))
cost_of_dream_home = float(input("Enter the cost of your dream house: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

months = 0
portion_down_payment = 0.25
down_payment = 0.25 * cost_of_dream_home
amount_saved = 0

monthly_salary = yearly_salary /12
monthly_saving = portion_saved * monthly_salary


###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
while amount_saved <= down_payment:
    additional = amount_saved * (0.05/12)
    amount_saved += monthly_saving
    amount_saved += additional
    months += 1
print(months)
