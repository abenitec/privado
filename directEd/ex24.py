#Python: Exception Handling

# Prompt the user to enter a value for x and convert it to an integer
try:
    x = int(input("What's x?"))
    # If the conversion is successful, print the value of x using an f-string
    print(f"x is {x}")
except ValueError:
    # If the conversion raises a ValueError, it means that the user entered a non-integer value. In this case, print an error message
    print("x is not an integer")