import sys
from ft_filter import ft_filter


def filter_words_by_length(s, n):
    assert isinstance(s, str) and isinstance(n, int)

    words = s.split()
    return list(ft_filter(lambda word: len(word) > n, words))


def main():
    try:
        # Checking the number of arguments
        assert len(sys.argv) == 3

        # Parsing command line arguments
        s = sys.argv[1]
        n = int(sys.argv[2])
        print(filter_words_by_length(s, n))

    except (AssertionError, ValueError):
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
