current_day = int(input("Current day number (0-6): "))
future_days = int(input("Number of days in the future: "))

new_day = (current_day + future_days) % 7

print("New day number is", new_day)
