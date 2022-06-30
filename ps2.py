'''balance = 5000
annualInterestRate = 0.18
monthlyPaymentRate = 0.02

for month in range(0,12):
    min_pay = balance * monthlyPaymentRate
    unpaid_balance = balance - min_pay
    paid_interest = unpaid_balance * (annualInterestRate/12)
    balance = round(unpaid_balance + paid_interest,2)

print("Remaining balance:", balance)'''


'''balance = 3926
annualInterestRate = 0.2
fixed_amount = 10
while fixed_amount < balance:
    start_balance = balance
    for month in range(0,12):
        unpaid_balance = start_balance - fixed_amount
        paid_interest = unpaid_balance * (annualInterestRate/12)
        start_balance = round(unpaid_balance + paid_interest,2)
    if start_balance <= 0:
        print(start_balance)
        break
    fixed_amount+=10


print("Lowest Payment:", fixed_amount)'''


balance = 320000
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate/12

lower_bound = balance/12
upper_bound = (balance * (1+monthlyInterestRate)**12)/12


while True:
    fixed_amount = round((lower_bound+upper_bound)/2,2)
    basic_balance = balance
    for month in range(0,12):
        unpaid_balance = basic_balance - fixed_amount
        paid_interest = unpaid_balance * (annualInterestRate/12)
        basic_balance = round(unpaid_balance + paid_interest,2)

    if basic_balance <= 0.1 and basic_balance >= -0.1:
        break
    elif basic_balance > 0.1:
        lower_bound = fixed_amount
    else:
        upper_bound = fixed_amount


print("Lowest Payment:", fixed_amount)