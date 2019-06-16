from CalculatorMethods import *
from InputMethods import *

total = 0
looper = True
while looper:
    print("\n" * 50)
    choice = menu(total)
    print("\n" * 50)

# ADD/SUB/MULT/DIV/PER ####################################
    if 1 <= choice <= 5:
        if not total:
            print("Enter the first number:")
            num1 = float_input()
        else:
            num1 = total
            print("The previous total is", num1)
        print("Enter the next number:")
        num2 = float_input()
        if choice == 1:
            total = addition(num1, num2)
        elif choice == 2:
            total = subtraction(num1, num2)
        elif choice == 3:
            total = multiplication(num1, num2)
        elif choice == 4:
            total = division(num1, num2)
        elif choice == 5:
            total = percent(num1, num2)
        print("The total is:", total)

# TRIG ####################################################
    elif choice == 6:
        if not total:
            print("Enter the number in radians as a decimal (without the pi):")
            num = float_input()
        else:
            num = total
        total = trig(num * math.pi)
        print("The total is:", total)

# DATABASE ################################################
    elif choice == 7:
        print("How many columns?")
        cols = int_input()
        print("How many rows?")
        rows = int_input()
        full_arr = []
        for col_num in range(1, 1 + cols):
            part_arr = []
            for row_num in range(1, 1 + rows):
                print("Enter the number for",str(col_num) + "," + str(row_num) + ":")
                part_arr.append(float_input())
            full_arr.append(part_arr)
        print(database(full_arr))

# GRAPH (Manual) ############################################
    elif choice == 8:
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

# GRAPH(COORDINATE POINTS) ################################
    elif choice == 9:
        print("How many coord points?")
        count = int_input()
        full_arr = []
        for i in range(count):
            print("Enter a point (x , y):")
            str_coord_point = input()
            a = tuple(map(float, str_coord_point.strip().split(",")))
            full_arr.append(a)

        tuplegrapher(full_arr)

# 1-VAR-STATS #############################################
    elif choice == 10:
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

# CLEAR ###################################################
    elif not choice:
        total = 0
        print("The total was reset")

# LOOPER ##################################################
    print("Enter (0) to quit")
    looper = bool(int_input())
