def calculate_str_length(b):
    """

    :rtype: Length of String
    """
    if type(b) == int:
        print("Sorry integers don't have length")
    elif type(b) == float:
        print("Sorry float don't have length")
    else:
        return len(b)


print(calculate_str_length(9.0))