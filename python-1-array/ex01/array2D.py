import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """slicing 2d array"""
    if not (isinstance(start, int) and isinstance(end, int)):
        print("start and end inputs must be int interger")
        return []
    if not (isinstance(family, list) and
            all(isinstance(row, list) for row in family)):
        print("input must be a list of list (2D array)")
        return []
    matrix = np.array(family)
    print(f"My shape is : {matrix.shape}")
    sliced_matrix = matrix[start:end]
    print(f"My new shape is : {sliced_matrix.shape}")
    sliced_matrix = sliced_matrix.tolist()
    return sliced_matrix
