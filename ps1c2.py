
annual_salary = float(input("Enter your annual salary:"))

total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = 0.25 * total_cost
r = 0.04

low = 0
high = 10000
guess = (low+high)/2

months_count = 0

epsilon = 0.0001
num_guess = 0

def calc_month(annual_salary,portion_saved):
    months_count = 0
    current_savings = 0
    salary = annual_salary
    portion_saved/=10000
    while current_savings < portion_down_payment:
        current_savings_r = current_savings*r/12
        current_savings_p = portion_saved*(salary/12)
        current_savings += current_savings_p + current_savings_r
        months_count += 1
        if months_count%6 == 0:
            salary += salary*semi_annual_raise
    return(months_count)


while abs(months_count - 36) > 0 and guess <= 10000:
    months_count = calc_month(annual_salary,guess)

    if months_count > 36:
        low = guess
    else:
        high = guess

    guess = (low+high)/2
    num_guess += 1

print (guess/10000, 'is the best portion to be saved\n')
print ('num_guesses=', num_guess,"\n")
        