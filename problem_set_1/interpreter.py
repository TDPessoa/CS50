"""Python already supports math, whereby you can write code to add, subtract, multiply, or divide values and even
variables. But let’s write a program that enables users to do math, even without knowing Python.

In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then
calculates and outputs the result as a floating-point value formatted to one decimal place. Assume that the user’s
input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:

x is an integer
y is +, -, *, or /
z is an integer
For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.

Note that, just as python itself is an interpreter for Python, so will your interpreter.py be an interpreter for
math! """


def main():
    user_input_str = str(input("What would you like me to interpret?")).split()

    x = user_input_str[0]
    y = user_input_str[1]
    z = user_input_str[2]

    if y == '+':
        print(float(int(x) + int(z)))
    elif y == '-':
        print(float(int(x) - int(z)))
    elif y == '*':
        print(float(int(x) * int(z)))
    elif y == '/':
        print(float(int(x) / int(z)))
    else:
        print('Opperator not recognized')


main()

"""This was the output of the build-in 'check50' function"""
# :) interpreter.py exists
# :) input of "1 + 1" yields output of 2.0
# :) input of "2 - 3" yields output of -1.0
# :) input of "2 * 2" yields output of 4.0
# :) input of "50 / 5" yields output of 10.0
# :) input of "3 / 2" yields output of 1.5
