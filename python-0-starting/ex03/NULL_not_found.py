def NULL_not_found(object: any) -> int:
    """null not found"""
    if object is None:
        print("Nothing: None", str(type(None)))
    elif type(object) is float and object != object:
        print("Cheese: nan", type(object))
    elif type(object) is int and object == 0:
        print("Zero: 0", type(object))
    elif type(object) is str and object == "":
        print("Empty:", type(object))
    elif type(object) is bool and object is False:
        print("Fake: False", type(object))
    else:
        print("Type not Found")
        return 1
    return 0

    # object != object is simillar to NaN, defined to be not
    # equal to itself
