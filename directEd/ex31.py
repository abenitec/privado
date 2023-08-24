# Define the hello function
def hello():
    # Prompt the user to enter their name and strip any whitespace and change it to title case 
    name = input("What's your name").strip().title()
    # Print a greeting message with the user's name
    print(f"Hello, {name}")

# Call the hello function
hello()