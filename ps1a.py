from sys import dont_write_bytecode


total_cost = float(input("Enter the cost of your dream home:"))
portion_saved = float(input("Enter the portion of your salary to be saved:"))
annual_salary = float(input("Enter your annual salary:"))


portion_down_payment = 0.25 * total_cost
current_savings = 0
r = 0.04
monthly_salary = annual_salary/12
months_count = 0

while current_savings < portion_down_payment:
    current_savings_r = current_savings*r/12
    current_savings_p = portion_saved*monthly_salary
    current_savings += current_savings_p + current_savings_r
    months_count += 1

print(months_count)