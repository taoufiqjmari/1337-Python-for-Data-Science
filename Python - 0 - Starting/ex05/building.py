import sys
import string


def counting(arg):
    """Counting type of characters of the argument"""
    upper = 0
    lower = 0
    punctuation = 0
    space = 0
    digit = 0

    for element in arg:
        if element.isupper():
            upper += 1
        elif element.islower():
            lower += 1
        elif element in string.punctuation:
            punctuation += 1
        elif element.isspace():
            space += 1
        elif element.isdigit():
            digit += 1

    print(f'The text contains {len(arg)} characters:')
    print(f'{upper} upper letters')
    print(f'{lower} lower letters')
    print(f'{punctuation} punctuation marks')
    print(f'{space} spaces')
    print(f'{digit} digits')


def building():
    """The main point of the program, handling arguments"""
    arg = ''

    try:
        assert len(sys.argv) > 2

        if len(sys.argv) == 1:
            arg = input('What is the text to count?\n')
        else:
            arg = sys.argv[1]

        counting(arg)
    except AssertionError:
        print('AssertionError: more than one argument is provided')


if __name__ == '__main__':
    building()
