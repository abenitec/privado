#Python: float

# Prompt the user to enter a value for x and convert it to a float
x = float(input("What's x? "))
# Prompt the user to enter a value for y and convert it to a float
y = float(input("What's y? "))

# Calculate the sum of x and y, round it to the nearest integer, and assign it to z
z = round(x + y)
# Calculate the quotient of x and y and assign it to a
a = x / y

# Print the value of z with comma separators
print(f"{z:,}")
# Print the value of a with two decimal places
print(f"{a:.2f}")