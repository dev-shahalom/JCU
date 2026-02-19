age = int(input("Enter your age: "))
if age < 18:
    print("You are not old enough to vote")
else:
    if age > 120:
        print("Invalid age")
    else:
        print("Vote for me Please")