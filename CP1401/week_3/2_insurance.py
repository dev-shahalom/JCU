age = int(input("Enter applicant age: "))

if age < 18:
    print("Hire refused")
elif age < 25:
    print("Insurance required")
else:
    print("Insurance not required")
