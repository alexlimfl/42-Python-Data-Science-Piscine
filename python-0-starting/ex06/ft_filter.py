# def ft_filter(function, lst):
#     filtered_lst = []
#     for item in lst:
#         if function(item):
#             filtered_lst.append(item)
#     return filtered_lst

def ft_filter(function, lst):
    """filters the string by function"""
    if function:
        return [item for item in lst if function(item)]
    return (lst)
