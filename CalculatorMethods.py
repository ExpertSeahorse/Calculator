from statistics import *
import pandas
import matplotlib.pyplot as plt
import math
from InputMethods import *


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
        return math.sin(num)
    elif op == 2:
        return math.cos(num)
    elif op == 3:
        return math.tan(num)
    elif op == 4:
        return 1 / math.cos(num)
    elif op == 5:
        return 1 / math.sin(num)
    elif op == 6:
        return 1 / math.tan(num)


def database(arr):
    """
    Creates a Pandas Database for use in graphing; akin to the stats button on a TI-84 Calculator
    :param arr:
    :return:
    """
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


def grapher(db, strng="Not", grid=False):
    """
    Graphs data based on data from pandas database func
    :param db:
    :param strng:
    :param grid:
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
    db.plot(kind=strng, x='x', y='y', rot=0, grid=grid)
    return plt.show()
