def count_in_list(lst, value):
    """counts the str in list"""
    count = 0
    for item in lst:
        if item == value:
            count += 1
    return count
