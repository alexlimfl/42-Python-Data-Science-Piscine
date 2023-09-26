import sys


def count_argv(argv):
    """counts argv"""
    count = 0
    for _ in argv[1:]:
        count += 1
    return count


def has_punctuation(input_str):
    """check if input_str has punctuation"""
    punctuation_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    for char in input_str:
        if char in punctuation_chars:
            return 1
    return 0


def count_char(input_str):
    """counts character in a string"""
    count = 0
    for char in input_str:
        count += 1
    return count


def split_words(input_str):
    """splits input_str into words"""
    lst = []
    start = 0
    str_len = count_char(input_str)
    while (start < str_len):
        while (start < str_len and input_str[start] == ' '):
            start += 1
        end = start
        while (end < str_len and input_str[end] != ' '):
            end += 1
        word = input_str[start:end]
        lst.append(word)
        start = end
    return lst


def filterlst_wlen(lst, input_len):
    """remove words in list less than len"""
    filtered_lst = []
    for item in lst:
        if count_char(item) > input_len:
            filtered_lst.append(item)
    return filtered_lst


def only_number(input_str):
    """checks if only number in the string"""
    for char in input_str:
        if not ('0' <= char <= '9'):
            return False
    return True


def filter_words_by_length(input_string, length):
    """using lamda function and comprehension expression"""
    words = input_string.split()
    filtered_words = [word for word in words if count_char(word) > length]
    return filtered_words


def main():
    try:
        if count_argv(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
        elif has_punctuation(sys.argv[1]):
            raise AssertionError("the arguments are bad")
        elif not only_number(sys.argv[2]):
            raise AssertionError("the arguments are bad")
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)
    # lst = split_words(sys.argv[1])
    # lst = filterlst_wlen(lst, int(sys.argv[2]))
    lst = filter_words_by_length(sys.argv[1], int(sys.argv[2]))
    print(lst)
    sys.exit(0)


if __name__ == "__main__":
    main()
