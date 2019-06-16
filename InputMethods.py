def float_input():
    type_match = False
    while not type_match:
        try:
            strin = float(input())
        except ValueError:
            print("Please enter a valid float")
        else:
            type_match = True
    return strin


def int_input():
    type_match = False
    while not type_match:
        try:
            strin = int(input())
        except ValueError:
            print("Please enter a valid int")
        else:
            type_match = True
    return strin
