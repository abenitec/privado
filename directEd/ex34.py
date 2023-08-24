#Python:Unit test

#Define a function main
def main():
    # Ask the user to input a value for x
    x = int(input("What's x? "))
    # Print the square of x
    print("x squared is ", square(x))

def square(n):
    # Return the square of n
    return n * n

if __name__ == "__main__":
    # Call the main function
    main()
