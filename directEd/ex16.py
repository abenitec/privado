#python Lists

students = ["Harmonie", "Harry", "Ron"]  # Create a list of strings called students
students.append("Abenezer")              # Add the string "Abenezer" to the end of the students list
students[0] = "Jack"                    # Replace the first element of the students list with the string "Jack"

for i in range(len(students)):          # Loop through the range of numbers from 0 to the length of the students list
    print(i + 1,".",students[i])        # Print the index of the current element plus 1, a period, and the current element

print(len(students))                    # Print the length of the students list