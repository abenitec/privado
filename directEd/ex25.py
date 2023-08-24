#Python : Exception handling

# Use a while loop to keep prompting the user until a valid integer is entered
while True:
# Prompt the user to enter a value for x and convert it to an integer
    try:
        x = int(input("What is x? "))
    except ValueError:
        # If the user enters a non-integer value, print an error message
        print("x is not an integer")
    else:
        # If the user enters an integer, break out of the loop
        break

# Print the value of x
print(f"x is {x}")