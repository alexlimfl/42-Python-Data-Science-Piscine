import sys


def only_alphanum(input_str):
    """check if str only has alphanumeric"""
    for char in input_str:
        if not char.isalnum() and not char.isspace():
            return False
    return True


def str_to_morse(input_str):
    """converts str to morse_code"""
    NESTED_MORSE = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.', ' ': '/'
    }
    lst = []

    for char in input_str:
        if char.islower():
            char = char.upper()
        try:
            if char not in NESTED_MORSE:
                raise AssertionError("the arguments are bad")
        except AssertionError as e:
            print(f"AssertionError: {e}")
            sys.exit(1)
        lst.append(NESTED_MORSE[char])
        lst.append(' ')
    return lst[:-1]


def main():
    """main"""
    try:
        if len(sys.argv) < 2:
            raise AssertionError("the arguments are bad")
        elif not only_alphanum(sys.argv[1]):
            raise AssertionError("the arguments are bad")
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)
    lst = str_to_morse(sys.argv[1])
    print(''.join(lst))
    sys.exit(0)


if __name__ == "__main__":
    main()
