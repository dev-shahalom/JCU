secret_number = 5
guess = int(input("Enter a number: "))
while guess != secret_number:
    print("You guessed it wrong")
    guess = int(input("Enter a number: "))
print("Well done, you guessed it")