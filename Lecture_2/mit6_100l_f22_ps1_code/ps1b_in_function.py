def part_b(yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise):
	#########################################################################
	
	portion_down_payment = 0.25
	down_payment = 0.25 * cost_of_dream_home
	amount_saved = 0
	
	months = 0
	monthly_salary = yearly_salary /12
	
	monthly_saving = portion_saved * monthly_salary
	
	###############################################################################################
	## Determine how many months it would take to get the down payment for your dream home below ## 
	###############################################################################################
	
	while amount_saved < down_payment:
	    additional = amount_saved * (0.05/12)
	    amount_saved += monthly_saving
	    amount_saved += additional
	    months += 1
	    if months % 6 == 0:
	        yearly_salary +=  (yearly_salary*semi_annual_raise)
	        monthly_salary = yearly_salary /12
	        monthly_saving = portion_saved * monthly_salary  
	print(months)
	return months