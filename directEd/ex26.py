#Python : Exception handling

# Define the main function
def main():
    # Call the get_int function to get an integer value for x
    x = get_int()
    # Print the value of x using an f-string
    print(f"x is {x}")

# Define the get_int function
def get_int():
    # Use a while loop to keep prompting the user until a valid integer is entered
    while True:
        try:
            # Use the int() function to convert the user's input to an integer
            # If the input is not an integer, a ValueError will be raised
            return int(input("What's x? "))
        except ValueError:
            # If a ValueError is raised, print an error message and prompt the user again
            print("x is not an integer")

# Call the main function to start the program
main()