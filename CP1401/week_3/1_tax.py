# Algorithm
# Get Total Income from User
# If total income < 100
# Tax is 0
# If Total income > 100
# Tax is 5%
# If Total Income > = 1000 
# Tax is 10% 
# Print Total Tax & Take Home Pay

# Code 
print("Python Party Tax Program")
total_income = float(input("Whats your total Income : "))

if total_income >= 1000 :
    tax_rate = 0.1
elif total_income>= 500:
    tax_rate = 0.02
elif total_income >100 :
    tax_rate = 0.05
else :
    tax_rate = 0

total_tax = total_income * tax_rate
take_home_pay = total_income - total_tax

print("Your Tax is $",total_tax,"& Your Take Home Pay after Tax is $",take_home_pay)