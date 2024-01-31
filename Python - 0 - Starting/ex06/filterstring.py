import sys
from ft_filter import ft_filter


def filter_words_by_length(s, n):
    """filter(string, integer) --> filter list

return a list with words from string longer than integer
    """
    words = s.split()
    return list(ft_filter(lambda word: len(word) > n, words))


def main():
    """The main point of the program, handling arguments"""
    try:
        # Checking the number of arguments
        assert len(sys.argv) == 3

        # Parsing command line arguments
        s = sys.argv[1]
        n = int(sys.argv[2])
        assert isinstance(s, str) and isinstance(n, int)

        print(filter_words_by_length(s, n))

    except (AssertionError, ValueError):
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
