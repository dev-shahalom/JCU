number = int(input("Enter a level number (1-16): "))

while number > 1 or number < 16:
    print("You are on level", number)
    number = int(input("Enter a level number (1-16): "))

print("Out of range")