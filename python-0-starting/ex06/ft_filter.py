# def ft_filter(function, lst):
#     filtered_lst = []
#     for item in lst:
#         if function(item):
#             filtered_lst.append(item)
#     return filtered_lst

def ft_filter(function, lst):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if function:
        return [item for item in lst if function(item)]
    return (lst)
