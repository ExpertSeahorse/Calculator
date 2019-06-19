from statistics import *
import pandas
import matplotlib.pyplot as plt
from math import *
from InputMethods import *
from numpy import arange
import re


def menu(total):
    """
    Is the menu for the calculator
    :param total:
    :return:
    """
    print("What would you like to do?")
    print("01. Addition\n"
          "02. Subtraction\n"
          "03. Multiplication\n"
          "04. Division\n\n"
          "05. Trig")
    if not total:
        print("06. Stats\n\n"
              "07. Create a database\n"
              "08. Graph(data points)\n"
              "09. Graph Coordinate Pairs\n"
              "10. Graph Equation")
    else:
        print("\n0. Clear"
              "\nTotal is:", total)

    return int_input()


def trig(num, op):
    """
    Calculates the sin/cos/tan/sec/csc/cot of a number in ***RAD***
    :param num:
    :param op:
    :return:
    """
    if op == 1:
        return sin(num)
    elif op == 2:
        return cos(num)
    elif op == 3:
        return tan(num)
    elif op == 4:
        return 1 / cos(num)
    elif op == 5:
        return 1 / sin(num)
    elif op == 6:
        return 1 / tan(num)


def database(arr, titles=False):
    """
    Creates a Pandas Database for use in graphing; akin to the stats button on a TI-84 Calculator
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


def stats_onevar(arr):
    avg = mean(arr)
    numsum = sum(arr)
    numsum2 = 0
    for entry in arr:
        numsum2 += entry**2
    sam_std = stdev(arr)
    pop_std = pstdev(arr)
    count = len(arr)
    minimum = min(arr)
    med = median(arr)
    maximum = max(arr)

    return avg, numsum, numsum2, sam_std, pop_std, count, minimum, med, maximum


def tuplegrapher(arr):
    """
    Creates a Pandas Database for use in graphing; accepts tuples for input
    :param arr:
    :return:
    """
    cols = ["x", "y"]
    db = pandas.DataFrame.from_records(arr, columns=cols)
    db.plot(kind='scatter', x=cols[0], y=cols[1])
    return plt.show()


def grapher(db, strng="Not", grid=False, xstep=None, ystep=None):
    """
    Graphs data based on data from pandas database func
    :param db:
    :param strng:
    :param grid:
    :param xstep:
    :param ystep:
    :return:
    """
    if strng == "Not":
        print("line : line plot (default)          bar : vertical bar plot\n",
              "barh : horizontal bar plot          hist : histogram\n",
              "box : boxplot                       kde : Kernel Density Estimation plot\n",
              "density : same as ‘kde’             area : area plot\n",
              "pie : pie plot                      scatter : scatter plot\n",
              "hexbin : hexbin plot\n\n")

        print('What type of graph?')
        strng = input().lower()
    columns = list(db.columns)
    # db.plot(kind=strng, x='x', y='y', rot=0, grid=grid, xticks=xstep, yticks=ystep)
    db.plot(kind=strng, x=columns[0], y=columns[1:], rot=0, grid=grid, xticks=xstep, yticks=ystep)
    return plt.show()


def equation_processor(eq: str, xmin: str, xmax: str, xstep: str):
    """
    Receives a string of a linear equation in the format y="Equation" with x or t as the dependent variable
    :param eq_string:
    :param xmax: @type: float
    :param xmin:
    :return:
    """
    # Checks if there is variables x and t present
    if 'x' in eq and 't' in eq:
        return "Cannot mix x and t variables"

    # Checks if the domain is unusable
    elif xmin >= xmax:
        return "Invalid Domain"

    # Checks if xstep is usable
    try:
        eval(xstep)
    except NameError:
        return "Invalid xstep"
    finally:
        str(xstep)

    input_group = [eq.lower(), xmin, xmax, xstep]
    err_code = re.compile(r' \w\(|\)\w|\w[a-z]|[a-z]\d')
    new_arr = []
    # for each of the passed parameters...
    for entry in input_group:
        # ***checks if the entry is only 1 character long
        if not (len(entry) - 1):
            new_arr.append(entry)
            continue

        # check through the entire length of the entry...
        for i in range(len(entry)-1):
            # if between two characters...
            eqw = entry[i] + entry[i+1]
            # there is one of the errors listed in the err_list...
            if err_code.match(eqw):
                # Add a multiplication symbol to fix the offence
                entry = entry[:i+1] + "*" + entry[i+1:]

        # And add the amended entry to this new list
        new_arr.append(entry)

    # Convert all parameters to a data type the grapher can use
    eq = new_arr[0].replace('x', '({x})').replace('t', '({x})').replace('^', '**')
    xmin = float(eval(new_arr[1]))
    xmax = float(eval(new_arr[2]))
    xstep = float(eval(new_arr[3]))

    x_arr = []
    y_arr = []
    d = abs(xmax / 1000)
    # Generate data points
    for xvar in arange(xmin, xmax, d):
        # If there is an error when sifting through the coordinate points, return an error
        try:
            yvar = eval(eq.format(x=xvar))
        except TypeError:
            return "No operator between characters"
        except ValueError:
            return "Invalid Domain"
        # Add the x and y values to the array's for pandas
        x_arr.append(xvar)
        y_arr.append(yvar)

    xtic = arange(xmin, xmax+xstep, xstep)
    grapher(db=database([x_arr, y_arr]), strng='line', grid=True, xstep=xtic)
