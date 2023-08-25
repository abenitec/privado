#Python: File I/O

name = input("What's ur name? ")

file = open("names.txt", "a")
# Write the user's name to the file
file.write(f"{name}\n")
file.close()
