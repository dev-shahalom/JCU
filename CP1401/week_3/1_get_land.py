# ALgorithm:
# Get inputs from user
# - Land Size
# - Price per square metre
# - Price of the house

# Land cost = Land Size * Price per square metre
# Total package cost = Land cost + Price of the house
# Display total package cost

# Program:
# Get inputs from user
land_size = float(input("Enter the size of the land in square metres: "))
price_per_sqm = float(input("Enter the price per square metre: "))
house_price = float(input("Enter the price of the house: "))

# Calculate land cost
land_cost = land_size * price_per_sqm

# Calculate total package cost
total_cost = land_cost + house_price

# Display result
print("Total cost of the package is: $", total_cost)