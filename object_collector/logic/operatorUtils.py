
def compare(operator, value1, value2):
    if operator == "GTE":
        return value1 >= value2
    elif operator == "GT":
        return value1 > value2
    elif operator == "LTE":
        return value1 <= value2
    elif operator == "LT":
        return value1 < value2
    elif operator == "EQUAL":
        return value1 == value2

    return False
