import sys
from ft_filter import ft_filter


def has_punctuation(input_str):
    """check if input_str has punctuation"""
    punctuation_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    for char in input_str:
        if char in punctuation_chars:
            return 1
    return 0


def main():
    """main"""
    try:
        if len(sys.argv) != 3:
            raise AssertionError("Two arguments required")
        text = sys.argv[1]
        if has_punctuation(text):
            raise AssertionError("special characters unallowed")
        n = int(sys.argv[2])
        if not (isinstance(text, str) and isinstance(n, int)):
            raise AssertionError("Invalid argument types")
        filtered = ft_filter(lambda item: len(item) > n, text.split())
        print(filtered)
    except ValueError:
        print("Error: second argument has to be an integer")
    except AssertionError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
