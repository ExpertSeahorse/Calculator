from CalculatorMethods import *
from InputMethods import *
from numpy import arange
# math is used when using eval to run equations
from math import *


def router(choice, total):
    print("\n" * 50)
    if 1 <= choice <= 4:
        statement, total = basicmath_driver(choice, total)
        print(statement)

    elif choice == 5:
        statement, total = trig_driver(total)
        print(statement)

    elif choice == 6:
        stat_driver()

    elif choice == 7:
        db_driver()

    elif choice == 8:
        man_graph_driver()

    elif choice == 9:
        tup_graph_driver()

    elif choice == 10:
        eq_graph_driver()

    elif not choice:
        print("The total was reset")
        total = 0

    if total:
        return total


def basicmath_driver(choice, total):
    if not total:
        print("Enter the first number:")
        num1 = float_input()
    else:
        num1 = total
        print("The previous total is", num1)
    print("Enter the next number:")
    num2 = float_input()
    if choice == 1:
        total = eval(str(num1) + "+" + str(num2))
    elif choice == 2:
        total = eval(str(num1) + "-" + str(num2))
    elif choice == 3:
        total = eval(str(num1) + "*" + str(num2))
    elif choice == 4:
        total = eval(str(num1) + "/" + str(num2))
    return "The total is: " + str(total), total


def trig_driver(total):
    if not total:
        print("Enter the number in radians as a decimal (without the pi):")
        num = float_input()
    else:
        print("Is the number in radians yet?")
        rad_tru = input().lower()
        if rad_tru[0] == 'y':
            num = total
        elif rad_tru[0] == 'n':
            num = (total / 180) * math.pi
    print("which operation do you want to preform on:", str(num) + "?\n",
          "1. sin\n 2. cos\n 3. tan\n 4. sec\n 5. csc\n 6. cot")
    op = int_input()
    while op not in range(1, 7):
        print("Please enter a value between 1 - 6")
        op = int_input()
    total = trig(num * math.pi, op)
    return "The total is: " + str(total), total


def db_driver():
    print("How many columns?")
    cols = int_input()
    print("How many rows?")
    rows = int_input()
    full_arr = []
    for col_num in range(1, 1 + cols):
        part_arr = []
        for row_num in range(1, 1 + rows):
            print("Enter the number for", str(col_num) + "," + str(row_num) + ":")
            part_arr.append(float_input())
        full_arr.append(part_arr)
    print(database(full_arr))


def man_graph_driver():
    print("How many columns?")
    cols = int_input()
    print("How many rows?")
    rows = int_input()
    full_arr = []
    for col_num in range(1, 1 + cols):
        part_arr = []
        for row_num in range(1, 1 + rows):
            print("Enter the number for", str(col_num) + "," + str(row_num) + ":")
            part_arr.append(float_input())
        full_arr.append(part_arr)
    print(database(full_arr))
    grapher(database(full_arr))


def tup_graph_driver():
    print("How many coord points?")
    count = int_input()
    full_arr = []
    for i in range(count):
        print("Enter a point (x , y):")
        str_coord_point = input()
        a = tuple(map(float, str_coord_point.strip().split(",")))
        full_arr.append(a)

    tuplegrapher(full_arr)


def stat_driver():
    print("How many entries of data?")
    rows = int_input()
    full_arr = []
    for row_num in range(rows):
        print("Enter a number:")
        full_arr.append(float_input())
    avg, numsum, numsum2, sam_std, pop_std, count, minimum, med, maximum = stats_onevar(full_arr)
    print("The average:", avg, "\n",
          "The sum:", numsum, "\n",
          "The sum of num**2:", numsum2, "\n",
          "The sample standard deviation:", sam_std, "\n",
          "The population standard deviation:", pop_std, "\n",
          "The n:", count, "\n",
          "The minimum:", minimum, "\n",
          "The median:", med, "\n",
          "The maximum:", maximum)


def eq_graph_driver():
    print("Acceptable functions:\n\n"
          "sin(x)\tt**z\n"
          "cos(t)\tsqrt(x)\n"
          "tan(x)\tlog(t)\n"
          "***The calculator requires notation such as:\n"
          "...##*x...##*(t)...\n")
    print("Enter the equation")
    eq = str(input())
    print("Enter the minimum x-value")
    x_min = float_input()
    print("Enter the maximum x-value")
    x_max = float_input()

    equation_processor(eq, x_min, x_max)


if __name__ == '__main__':
    total = 0
    looper = True
    while looper:
        print("\n" * 50)
        total = router(menu(total), total)
        print("Enter (0) to quit, or any other key to continue")
        looper = bool(int_input())
