#python :Functions

# Define a main function that calls the hello function with user input
def main():
    # Ask for the user's name and call the hello function with the input
    name = input("What's your name? ")
    hello(name)

    # Call the hello function without passing any arguments
    hello()

# Define a function that asks for the user's name and greets them
def hello(myName="Abenezer"):
    print("hello,", myName)

# Call the main function
main()
