def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """gets BMI"""
    if len(height) <= 0 or len(weight) <= 0:
        print("Error: Empty list")
        return []
    if len(height) != len(weight):
        print("Error: list size of height and weight not same")
        return []
    bmi_lst = []
    for h, w in zip(height, weight):
        if not (isinstance(h, (int, float)) and isinstance(w, (int, float))):
            print("Error: Values are not int or float")
            return []
        if h <= 0 or w <= 0:
            print("Error: Values are not positive")
            return []
        bmi = w / (h * h)
        bmi_lst.append(bmi)
    return bmi_lst

# We use a for loop with the zip() function to iterate
# through both lists simultaneously. zip() combines elements from
# both lists into pairs."


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """provides check to BMI limit stated"""
    if len(bmi) == 0:
        print("Error: Empty list")
        return []
    if not (isinstance(limit, int) and limit >= 0):
        print("Error: Value(limit) are not int or positive")
        return []
    output_lst = []
    for b in bmi:
        if not isinstance(b, (int, float)):
            print("Error: Values(bmi) are not int or float")
        if b > limit:
            output_lst.append(True)
        else:
            output_lst.append(False)
    return output_lst
