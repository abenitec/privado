#Python: File I/O

#Create empty list in variable called names
names = []

for i in range(3):
    # Ask the user for their name and append it to the list of names
    names.append(input("What's your name? "))

for name in sorted(names):               
    # Print each name in the sorted list of names
    print(name)
