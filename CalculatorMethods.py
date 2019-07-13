from statistics import median, mean, pstdev, stdev
from NumberValidation import *
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


def stats_onevar(arr):
    """
    Run a variety of stats functions on a list of numbers
    :param arr:
    :return:
    """
    # Takes the average
    avg = mean(arr)
    # Finds ths sum of all of the numbers
    numsum = sum(arr)
    # Finds the sum of all of the numbers squared
    numsum2 = sum(num**2 for num in arr)
    # Finds the sample standard deviation
    sam_std = stdev(arr)
    # Finds the population standard deviation
    pop_std = pstdev(arr)
    # Finds the number of values
    count = len(arr)
    # Finds the minimum value
    minimum = min(arr)
    # Finds the median value
    med = median(arr)
    # Finds the maximum value
    maximum = max(arr)

    # Returns all of the variables
    return avg, numsum, numsum2, sam_std, pop_std, count, minimum, med, maximum


def tuple_grapher(arr):
    """
    Creates a Pandas Database for use in graphing; accepts only tuples for input
    :param arr:
    :return:
    """
    # Sets the column titles
    cols = ["x", "y"]
    # Creates a pandas DB using the list of tuples
    db = pandas.DataFrame.from_records(arr, columns=cols)
    # Plots the DB
    db.plot(kind='scatter', x=cols[0], y=cols[1])
    # Displays the graph
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
    # If no graph was chosen...
    if strng == "Not":
        # here are the options and pick one
        print("line : line plot (default)          bar : vertical bar plot\n",
              "barh : horizontal bar plot          hist : histogram\n",
              "box : boxplot                       kde : Kernel Density Estimation plot\n",
              "density : same as ‘kde’             area : area plot\n",
              "pie : pie plot                      scatter : scatter plot\n",
              "hexbin : hexbin plot\n\n")

        print('What type of graph?')
        strng = input().lower()
    # Gets the column names from the db
    columns = list(db.columns)
    # Old plot command
    # db.plot(kind=strng, x='x', y='y', rot=0, grid=grid, xticks=xstep, yticks=ystep)
    # Plots the DB
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
    mult_err_code = re.compile(r' \w\(|\)\w|\w[a-z]|[a-z]\d')
    new_arr = []
    # for each of the passed parameters...
    for entry in input_group:
        # Run through the expression converter
        entry = expression_converter(entry)
        # And add the converted expressions to the array
        new_arr.append(entry)

    # Convert all parameters to a data type the grapher can use
    eq = new_arr[0].replace('x', '({x})').replace('t', '({x})')
    xmin = float(eval(new_arr[1]))
    xmax = float(eval(new_arr[2]))
    xstep = float(eval(new_arr[3]))

    x_arr = []
    y_arr = []
    d = abs(xmax / 1000)
    # Generate data points
    for xvar in arange(xmin, xmax, d):
        # Plug a value for x into the equation
        try:
            yvar = eval(eq.format(x=xvar))
        except TypeError:
            # If there is an issue from having incorrectly formatted eq (fixed by the expr converter)
            return "No operator between characters"
        except ValueError:
            # If the xmin or xmax are invalid for a function
            return "Invalid Domain"
        # Add the x and y values to the array's for pandas
        x_arr.append(xvar)
        y_arr.append(yvar)

    # Makes the tic marks on the graph
    xtic = arange(xmin, xmax+xstep, xstep)
    # Pushes the array of x and y positions into a database and graphs it
    grapher(db=database([x_arr, y_arr]), strng='line', grid=True, xstep=xtic)
