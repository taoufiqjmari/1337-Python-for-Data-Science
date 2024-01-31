import sys

try:
    assert len(sys.argv) <= 2

    if len(sys.argv) == 2:
        if int(sys.argv[1]) % 2:
            print("I'm Odd")
        else:
            print("I'm Even")

except AssertionError:
    print('AssertionError: more than one argument is provided')
except ValueError:
    print('AssertionError: argument is not an integer')
