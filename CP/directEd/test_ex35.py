# Import the function hello from ex35 module
from ex35 import hello

def main():
    test_hello()

def test_hello():
    assert hello() == "hello, world"
    assert hello("David") == "hello, David"

if __name__  == "__main__":
    # Call the main function
    main()


