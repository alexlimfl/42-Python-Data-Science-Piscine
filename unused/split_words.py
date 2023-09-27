def split_words(input_string):
    """Splits a string into words."""
    lst = []
    start = 0

    while start < len(input_string):
        while start < len(input_string) and input_string[start] == ' ':
            start += 1

        end = start
        while end < len(input_string) and input_string[end] != ' ':
            end += 1

        word = input_string[start:end]
        lst.append(word)
        start = end

    return lst

# Example usage
text = "This is a sample sentence."
word_list = split_words(text)
print(word_list)
