#Python : Function

# Define a main function
def main():
    # Call the print_square function with an argument of 3
    print_square(3)

# Define a function called print_square that takes a size parameter
def print_square(size):
    # Iterate over each row in the square
    for i in range(size):
        # Call the print_row function with the width equal to the size
        print_row(size)

# Define a function called print_row that takes a width parameter
def print_row(width):
    # Print a row of '#' characters with a length equal to the width
    print("#" * width)

# Call the main function to start the program
main()

