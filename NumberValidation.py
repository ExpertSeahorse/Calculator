import re
import pandas


def expression_converter(expr):
    """
    Replaces #(, )#, #x, x#, and ^ with the equivalent in python
    :param expr:
    :return:
    """
    expr = str(expr)
    mult_err_code = re.compile(r'\w\(|\)\w|\w[a-z]|[a-z]\d')

    # if the entry is only 1 character long...
    if not (len(expr) - 1):
        # there can't be an error with only one number
        return expr

    # check through every char in the entry...
    for i in range(len(expr) - 1):
        # if between two characters...
        eqw = expr[i] + expr[i + 1]
        # there is one of the errors listed in the err_list...
        if mult_err_code.match(eqw):
            # Add a multiplication symbol to fix the offence
            expr = expr[:i + 1] + "*" + expr[i + 1:]

    # And add the fixed entry to this new list and replaces all of the '^'s with '**'s
    return expr.replace('^', '**')


def database(arr, titles=False):
    """
    Creates a Pandas Database for use in graphing; akin to the stats button on a TI-84 Calculator
    Also used to transform an array into a DB for graphing
    :param arr:
    :param titles:
    :return:
    """
    if not titles:
        if isinstance(arr[0], list) or isinstance(arr[0], tuple):
            if len(arr) == 2:
                indx = ["x", "y"]
            elif len(arr) == 3:
                indx = ["x", "y", "z"]
            else:
                indx = range(1, len(arr) + 1)
            cols = range(1, len(arr[0])+1)

        elif isinstance(arr[0], float):
            indx = ["y"]
            cols = range(1, len(arr)+1)

        else:
            indx = range(1, len(arr) + 1)
            cols = range(1, len(arr[0])+1)
    else:
        indx = titles
        cols = range(1, len(arr[0]) + 1)

    return pandas.DataFrame(arr, index=indx, columns=cols).T

