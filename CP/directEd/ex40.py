# Define a class named Student
class Student:
    # Define the __init__ method that initializes the object with name and house attributes
    def __init__(self, name, house):
        self.name = name
        self.house = house

# Define the main function
def main():
    # Call the get_student function to get a student object
    student = get_student()
    # Print the name and house of the student
    print(f"{student.name} from {student.house}")

# Define the get_student function
def get_student():
    # Prompt the user to enter the name and house of the student
    name = input("Name: ")
    house = input("House: ")
    # Create a new Student object with the entered name and house
    student = Student(name, house)
    # Return the student object
    return student

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Call the main function
    main()
