import tkinter as tk
from CalculatorMethods import trig, grapher, database, stats_onevar, tuplegrapher, equation_processor
import math


class CalcMenu:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator GUI")

        self.label = tk.Label(master)
        self.label.grid(columnspan=2, sticky=tk.W)

        button_parts = [("math_button", "Basic Math", lambda: self.router(1), 1, 0, 1),
                        ("trig_button", "Trig", lambda: self.router(2), 1, 1, 1),
                        ("stat_button", "Stats", lambda: self.router(3), 2, 0, 1),
                        ("man_graph_button", "Manual Graph", lambda:self.router(4), 2, 1, 1),
                        ("coord_graph_button", "Coord Point Graph", lambda:self.router(5), 3, 0, 1),
                        ("equation_graph_button", "Equation Graph", lambda:self.router(6), 3, 1, 1),
                        ("quit_button", "Quit", master.quit, 4, 0, 2)]

        for name, label, comm, row, col, colspan in button_parts:
            if colspan == 2:
                wid = 40
            else:
                wid = 20
            self.name = tk.Button(master, text=label, width=wid, command=comm)
            self.name.grid(row=row, column=col, columnspan=colspan)

    def router(self, num):
        self.newWindow = tk.Toplevel(self.master)
        if num == 1:
            self.app = FiveFunc(self.newWindow)
        elif num == 2:
            self.app = TrigFunc(self.newWindow)
        elif num == 3:
            self.app = StatFunc(self.newWindow)
        elif num == 4:
            self.app = ManGraph(self.newWindow)
        elif num == 5:
            self.app = TupGraph(self.newWindow)
        elif num == 6:
            self.app = EqGraph(self.newWindow)
########################################################################################################################


class FiveFunc:
    def __init__(self, master):
        self.title = tk.Label(master, text="Your Expression:").pack()
        self.entry = tk.Entry(master)
        self.entry.bind("<Return>", self.evaluate)
        self.entry.pack()
        self.res = tk.Label(master)
        self.res.pack()

    def evaluate(self, event):
        self.res.configure(text="Result: " + str(eval(self.entry.get())))
########################################################################################################################


class TrigFunc:
    def __init__(self, master):
        self.title = tk.Label(master, text="Enter the number in rad/pi").pack()
        # This makes the expression entry field
        self.e1 = tk.Entry(master)
        self.e1.pack()
        tk.Label(master, text="Pick the Operation:").pack()

        # This makes the radio buttons
        var = tk.IntVar()
        radiolist = [("trigsin", "Sin", 1, lambda: self.sel(var.get())),
                     ("trigcos", "Cos", 2, lambda: self.sel(var.get())),
                     ("trigtan", "Tan", 3, lambda: self.sel(var.get())),
                     ("trigsec", "Sec", 4, lambda: self.sel(var.get())),
                     ("trigcsc", "Csc", 5, lambda: self.sel(var.get())),
                     ("trigcot", "Cot", 6, lambda: self.sel(var.get()))]
        for name, label, val, comm in radiolist:
            self.name = tk.Radiobutton(master, text=label, variable=var, value=val, command=comm)
            self.name.pack()

        # This is the output line
        self.res = tk.Label(master)
        self.res.pack()

    def sel(self, op):
        a = eval(self.e1.get())*math.pi
        b = trig(a, op)
        self.res.config(text=str(b))
########################################################################################################################


class StatFunc:
    def __init__(self, master):
        fieldlist = [("entlab", "Enter the list of numbers, separated by commas", "list_entry")]
        self.new_list = []
        for a, b, c in fieldlist:
            self.a = tk.Label(master, text=b)
            self.a.pack()
            self.c = tk.Entry(master)
            self.c.bind("<Return>", self.stat_runner)
            self.c.pack()
            self.new_list.append(self.c)

        self.res = tk.Label(master)
        self.res.pack()

    def stat_runner(self, event):
        avg, numsum, numsum2, sam_std, pop_std, count, minimum, med, maximum \
            = stats_onevar(list(map(float, (str(self.new_list[0].get())).split(','))))

        self.res.config(text="The average:" + str(avg) + "\n" +
                             "The sum: " + str(numsum) + "\n" +
                             "The sum of num**2: " + str(numsum2) + "\n" +
                             "The sample standard deviation: " + str(sam_std) + "\n" +
                             "The population standard deviation: " + str(pop_std) + "\n" +
                             "The n: " + str(count) + "\n" +
                             "The minimum: " + str(minimum) + "\n" +
                             "The median: " + str(med) + "\n" +
                             "The maximum: " + str(maximum), justify=tk.LEFT)


########################################################################################################################


class ManGraph:
    def __init__(self, master):
        fieldlist = [("xlabel", "Enter the values of the x-axis of the graph separated by commas", "x_entry"),
                     ("ylabel", "Enter the values of the y-axis of the graph separated by commas", "y_entry"),
                     ("graph_type", "Enter the type of graph you want", "graph_entry")]
        self.new_list = []
        for a, b, c in fieldlist:
            self.a = tk.Label(master, text=b)
            self.a.pack()
            self.c = tk.Entry(master)
            self.c.bind("<Return>", self.db_converter)
            self.c.pack()
            self.new_list.append(self.c)
        self.options = tk.Label(master, text="line\t: line plot\t\tbar\t: vertical bar plot\n"
                                     "barh\t: horizontal bar plot\thist\t: histogram\n"
                                     "box\t: boxplot\t\t\tkde\t: Kernel Density Estimation plot\n"
                                     "area\t: area plot\t\tpie\t: pie plot\n"                      
                                     "scatter\t: scatter plot\t\thexbin\t: hexbin plot", justify=tk.LEFT)
        self.options.pack()

    def db_converter(self, event):
        # gets the input out of the entry field, forces it into a string, splits it into a list,
        # then tries to map all of the list entries into a float: If fail, keeps the values as strings
        try:
            x_values = list(map(float, (str(self.new_list[0].get())).split(',')))
        except ValueError:
            x_values = str(self.new_list[0].get()).split(',')
        try:
            y_values = list(map(float, (str(self.new_list[1].get())).split(',')))
        except ValueError:
            y_values = str(self.new_list[1].get()).split(',')
        grapher(database([x_values, y_values]), self.new_list[2].get())
########################################################################################################################


class TupGraph:
    def __init__(self, master):
        self.input_list = []
        self.label = tk.Label(master, text="Enter the coordinate points: \"###,### ; ###,###\"").pack()
        self.input = tk.Entry(master)
        self.input.bind("<Return>", self.db_converter)
        self.input.pack()
        self.input_list.append(self.input)

    def db_converter(self, event):
        arr = str(self.input_list[0].get()).strip().split(';')
        for i, entry in enumerate(arr):
            newentry = tuple(map(float, entry.strip().split(",")))
            arr[i] = newentry
        tuplegrapher(arr)
########################################################################################################################


class EqGraph:
    def __init__(self, master):
        self.input_list = []
        self.label = tk.Label(master, text="Equation Graphing")
        self.label.grid(columnspan=2, sticky=tk.N)

        entry_list = [("input", "", "Enter the equation", "a"),
                      ("win_min", "-10", "Enter the min x-value", "b"),
                      ("win_max", "10", "Enter the max x-value", "c")]
        row = 1
        for a, deftxt , labtxt, labname in entry_list:
            self.labname = tk.Label(master, text=labtxt).grid(row=row)
            self.a = tk.Entry(master)
            self.a.bind("<Return>", self.eq_converter)
            self.a.insert(tk.END, deftxt)
            self.a.grid(row=row, column=1)
            self.input_list.append(self.a)
            row += 1

    def eq_converter(self, event):
        eq = str(self.input_list[0].get())
        x_min = float(self.input_list[1].get())
        x_max = float(self.input_list[2].get())
        equation_processor(eq, x_min, x_max)


if __name__ == '__main__':
    root = tk.Tk()
    app = CalcMenu(root)
    root.mainloop()
