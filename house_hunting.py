annual_salary = int(input("What is your annual salary? "))
portion_saved = float(input("What portion, in decimal form, would you like to save? "))
total_cost = int(input("How much does your dream home cost? "))
goal_down_payment = int(total_cost * 0.25)
monthly_payment = int(portion_saved * annual_salary/12)
r = .04
current_savings = 0
number_of_months = 0

while current_savings < goal_down_payment:
    number_of_months = number_of_months + 1
    current_savings = current_savings + monthly_payment + (current_savings*r/12)


print(number_of_months)



