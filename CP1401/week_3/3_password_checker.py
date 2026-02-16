# Password Checker

secret_password = "passme"

user_password = input("Enter Secret Password: ")
if user_password == secret_password:
    print("Access granted")
else:
    print("Access denied")
