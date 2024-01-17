import sys


NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. "
}


def morsify(string):
    output = ''

    for letter in string:
        output += NESTED_MORSE[letter]
    return output


def main():
    try:
        assert len(sys.argv) == 2, "len"
        assert all(c.isalnum() for c in sys.argv[1])

        string = sys.argv[1].upper()
        print(morsify(string)[:-1])
    except AssertionError:
        print('AssertionError: the arguments are bad')


if __name__ == "__main__":
    main()
