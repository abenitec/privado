#Python: File I/O

# Create empty list and store it in variable names
names = []

with open("names.txt") as file:
    # Read each line of the file and append it to the list of names
    for line in file:
        names.append(line.strip())

for name in sorted(names):
    # Print a greeting with each name in the sorted list of names
    print(f"hello, {name}")
