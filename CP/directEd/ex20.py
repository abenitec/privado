#Python : Function

# Define a main function
def main():
    # Ask the user for the value of x and store it in the variable x
    x = int(input("What's x? "))
    # Print the square of x by calling the square function
    print("x squared is", square(x))

# Define a function called square that takes a number as input and returns its square
def square(n):
    return n * n

# Call the main function to start the program
main()

#================= The file with the error ===================================

'''def main():
    x = int(input("What's x? "))
    print("x squared is", square(x,3)) #the error is in this line that square() takes 1 positional argument but 2 were given
def square(n):
    return n * n

main()'''