
annual_salary = float(input("Enter your annual salary:"))

total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = 0.25 * total_cost
r = 0.04


for i in range(1,10000):
    months_count = 0
    current_savings = 0
    salary = annual_salary
    portion_saved = i/10000
    while current_savings < portion_down_payment:
        current_savings_r = current_savings*r/12
        current_savings_p = portion_saved*(salary/12)
        current_savings += current_savings_p + current_savings_r
        months_count += 1
        if months_count%6 == 0:
            salary += salary*semi_annual_raise
    if months_count == 36 :
        print(portion_saved)