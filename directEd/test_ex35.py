# Import the function hello from ex35 module
from ex35 import hello

def main():
    # Call the test_default and test_argument functions
    test_default()
    test_argument()

def test_default():
    # Test the hello function with no arguments
    try:
        assert hello() == "hello, world"
    except:
        print("Default isn't printing \"hello, world\"")

def test_argument():
    # Test the hello function with an argument
    try:
        assert hello("Abenezer") == "hello, Abenezer"
    except:
        print("There is code problem")

if __name__  == "__main__":
    # Call the main function
    main()


