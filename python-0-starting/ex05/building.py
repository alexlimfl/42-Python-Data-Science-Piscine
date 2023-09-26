import sys


def count_char(string):
    """counts character in a string"""
    count = 0
    for char in string:
        count += 1
    return count


def count_lower(string):
    """counts lowercase in a string"""
    count = 0
    for char in string:
        if char.islower():
            count += 1
    return count


def count_upper(string):
    """counts uppercase in a string"""
    count = 0
    for char in string:
        if char.isupper():
            count += 1
    return count


def count_digit(string):
    """counts digit in a string"""
    count = 0
    for char in string:
        if char.isdigit():
            count += 1
    return count


def count_punctuation(string):
    """counts punctuation in a string"""
    punctuation_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    count = 0
    for char in string:
        if char in punctuation_chars:
            count += 1
    return count


def count_space(string):
    """counts space in a string"""
    count = 0
    for char in string:
        if char.isspace():
            count += 1
    return count


def count_argv(argv):
    """counts argv"""
    count = 0
    for _ in argv[1:]:
        count += 1
    return count


def main():
    try:
        if count_argv(sys.argv) > 1:
            raise AssertionError("more than one argument")
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)
    if count_argv(sys.argv) < 1:
        input = "Hello World! "
        print("What is the text to count?\n" + input)
    else:
        input = sys.argv[1]
    print(f"The text contains {count_char(input)} characters:")
    print(f"{count_upper(input)} upper letters")
    print(f"{count_lower(input)} lower letters")
    print(f"{count_punctuation(input)} punctuation marks")
    print(f"{count_space(input)} spaces")
    print(f"{count_digit(input)} digits")
    sys.exit(0)


if __name__ == "__main__":
    main()
