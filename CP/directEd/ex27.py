#Python : Exception Handling

# Define the main function
def main():
    # Call the get_int function with a prompt and assign the result to x
    x = get_int("What's x? ")
    # Print the value of x using formatted string
    print(f"x is {x}")
          
# Define the get_int function that takes a prompt as a parameter
def get_int(prompt):
    # Use a while loop to keep asking for input until a valid integer is entered
    while True:
        # Use a try-except block to handle ValueError exception
        try:
            # Return the input converted to an integer
            return int(input(prompt))
        except ValueError:
            # If the input is not an integer, ignore it and continue the loop
            pass

# Call the main function
main()
