import math
import matplotlib.pyplot as plt
import numpy as np

def solve_expression(x_values, expression):
    y_values = [max(0, expression(x)) for x in x_values]
    return y_values

def write_to_file(x_values, y_values_dict):
    with open("output_values.txt", "w") as file:
        for expression_name, values in y_values_dict.items():
            file.write(f"{expression_name}:\n")
            for value in values:
                file.write(f"{int(round(value))}\n")
            file.write("\n")

def plot_expression(x_values, y_values, expression_name):
    plt.plot(x_values, y_values, label=expression_name, linewidth=2)

def plot_all_expressions(x_values, y_values_dict):
    plt.figure(figsize=(12, 8))
    for expression_name, y_values in y_values_dict.items():
        plot_expression(x_values, y_values, expression_name)
    plt.title("Graph of All Expressions")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(left=0)
    plt.ylim(bottom=0)
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.show()

x_values = np.linspace(1, 50, 100)

expressions = {}
with open("input2.txt", "r") as file:
    for line in file:
        name, expr = line.strip().split(":")
        expressions[name.strip()] = lambda x, e=expr: eval(e)

def display_expressions():
    print("Available Expressions:")
    for i, expression_name in enumerate(expressions.keys()):
        print(f"{i + 1}. {expression_name}")
    print("11. Show All Graphs")
    print("0. Quit")

while True:
    display_expressions()
    choice = input("\nEnter the number of the expression you want to plot (or 11 to show all graphs, or 0 to quit): ")

    if choice == '0':
        print("Goodbye!")
        break

    try:
        choice = int(choice)

        if choice == 11:
            y_values_dict = {}
            for expression_name, expression_func in expressions.items():
                y_values_dict[expression_name] = solve_expression(x_values, expression_func)
            plot_all_expressions(x_values, y_values_dict)
            write_to_file(x_values, y_values_dict)

        elif 1 <= choice <= len(expressions):
            expression_name = list(expressions.keys())[choice - 1]
            expression = expressions[expression_name]
            y_values = solve_expression(x_values, expression)
            plot_expression(x_values, y_values, expression_name)
            plt.title(f"Graph of {expression_name}")
            plt.xlabel('x')
            plt.ylabel('y')
            plt.xlim(left=0)
            plt.ylim(bottom=0)
            plt.legend(loc='upper left')
            plt.grid(True)
            plt.show()
            plot_all_expressions(x_values, expressions)
            write_to_file(x_values, expressions)

        else:
            print("Invalid choice. Please enter a number between 1 and", len(expressions), "or 11.")

    except ValueError:
        print("Invalid input. Please enter a number or 0 to quit.")
