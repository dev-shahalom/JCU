# Get Salary and Years 
salary = float(input("Enter your Salary: "))
years_on_job = float(input("Enter the years that you are doing the Job : "))

# Check the Salary And Year 
if salary >= 30000 :
    if years_on_job >= 2 :
        print("You are eligible for the Loan")
    else:
        print("You must be employed for atleast for 2 Years")
else:
    print("You need to earn more than 30000$")

