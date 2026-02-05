# Get the base food cost from user
original_food_cost = float(input("Enter the original food cost: $"))
# Get the surcharge percentage from user
surcharge_percentage = float(input("Enter the percentage of the surcharge: "))
# Calculate the surcharge amount
surcharge_amount = original_food_cost * surcharge_percentage
# Add surcharge to original cost to get total
total_cost = original_food_cost + surcharge_amount
# Display the final cost with 2 decimal places
print(f"The surcharge amount of the meal is ${total_cost:.2f}")