#Python: Unit test

#import square function from ex34 module
from ex34 import square

def main():
    # Call the test_square function
    test_square()

def test_square():
    # Test the square function with different inputs
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared is not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared is not 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 squared is not 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 squared is not 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared is not 0")
    else:
        print("All test passed! ex34.py is working correctly!!")
    
if __name__  == "__main__":
    # Call the main function
    main()

