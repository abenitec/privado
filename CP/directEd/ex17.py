# Define a list of students with their attributes
students = [
    {"name": "Hermoine", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

# Iterate over each student in the list
for student in students:
    # Print the name, house, and patronus of each student
    print(student["name"], student["house"], student["patronus"], sep=", ")