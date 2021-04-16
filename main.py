"""Calculator For Random Things"""
__author__ = "Khushi Patel"

import math


def welcome_message():
    """
    This function asks the user for their name in order to print a
    welcome message.
    """
    print("Welcome to the calculator.")
    name = input("What is your name? ")
    print("Let's get started, " + name + "! ", end='\n\n')


def addition(num1, num2):
    """
    This function caclulates the sum of two numbers.
    :param num1: First addend, inputed by the user as a number
    :param num2: Second addend, inputed by the user as a number
    :return: The sum of num1 and num2
    """
    sum = num1 + num2
    print("The sum is ", sum, ".\n", sep="")


def subtraction(num1, num2):
    """
    This function caclulates the difference between two numbers
    :param num1: First number inputed by the user, as a number.
    :param num2: Amount being subtracted from num1, as a number.
    :return: Difference between num1 and num2
    """
    difference = num1 - num2
    return difference


def division(num1, num2):
    """
    This function calculates the quotient of two numbers and prints either the
    quotient
    the whole number and remainder, separately.
    :param num1: The dividend, entered by the user as a number
    :param num2: The divisor, entered by the user as a number.
    """
    choice = input(
        "Would you like \na) a quotient or \nb) the remainder and whole "
        "number?\n")
    # only returns the quotient as a decimal
    if choice == "a" or choice == "A":
        quotient = num1 / num2
        print("The quotient is ", quotient, ".", sep="")
    # returns the integer portion of the quotient and the remainder
    elif choice == "B" or choice == "b":
        remainder = num1 % num2
        print("The remainder is, ", remainder, ".", sep="")
        integer_portion = num1 // num2
        print("Floor division: ", integer_portion, ".\n", sep="")


def multiplication(num1, num2):
    """
    This function calculates the product of two numbers
    :param num1: First multiplier, entered by the user as a number.
    :param num2: Second multiplier, entered by the user as a number.
    :return: The product of num1 and num2
    """
    product = num1 * num2
    return product


def exponents(num1, num2):
    """
    This function calculates num1 to the power of num2
    :param num1: The base, entered by the user as a number.
    :param num2: The exponent, entered by the user as a number.
    :return: The product of num1 to the power of num2.
    """
    product = num1 ** num2
    return product


def circle_area(radius):
    """
    This function calculates the area of a circle.
    :param radius: The radius given the by the user, as a number.
    :return: The area of the circle
    """
    area = radius ** 2 * math.pi
    return area


def cube_area(side_length):
    """
    This function calculates the area of a cube.
    :param side_length: The length of one side of the cube, as a number.
    :return: The area of the cube.
    """
    area = side_length ** 3
    return area


def inequalities(num1, num2):
    """
    This function compares two numbers and prints an inequality.
    :param num1: The first number to be compared in the inequality
    :param num2: The second number to be compared in the inequality
    """
    if num1 < num2:
        print(num1, " is less than ", num2, sep="")
    elif num1 == num2:
        print(num1, "is equal to ", num2, sep="")
    elif num1 > num2:
        print(num1, " is great than ", num2, sep="")
    else:
        print("Could not compute an inequality.")


def range_function(num, start_range, end_range):
    """
    This function checks to see if a number is in a certain range, entered
    by the user.
    :param num: The number being checked to see if it is in the range
    :param start_range: The lower end of the range
    :param end_range: The higher end of the range
    """
    if num > start_range and num < end_range:
        print(num, "is in the range.\n")
    elif num < start_range or num > end_range:
        print(num, "is not in the range.\n")


def main():
    """
    The main function provides the user with a list of calculations to
    choose from, takes the user's input, and performs calculations based on
    the function corresponding to the choice the user made.
    """
    welcome_message()
    continue_program = True
    num_calculations = 0
    # all the calculation options in the program
    calculation_options = ["addition", "subtraction", "division",
                           "multiplication", "exponents", "circle area",
                           "cube area",
                           "repeat words", "inequalities", "in-range",
                           "stop program"]

    while continue_program:
        print("Enter the option number of the calculation you would like to "
              "perform: ")
        # prints the calculations options list as a numbered list
        for calculation in calculation_options:
            print(calculation_options.index(calculation) + 1, ". ",
                  calculation, sep="")

        while True:
            try:
                user_input = int(input(""))
                break
            except ValueError:
                print(
                    "That was not a valid input. Please enter a whole number "
                    "between 1 and 11.")

        if user_input in range(1, 12):
            if user_input == 1:  # addition
                run_addition = True
                while run_addition:
                    try:
                        user_num1 = float(input("Enter the first number: "))
                        user_num2 = float(input("Enter the second number: "))
                        addition(user_num1, user_num2)
                        run_addition = False
                    except ValueError:
                        print("That was not a valid input.")

            elif user_input == 2:  # subtraction
                run_subtraction = True
                while run_subtraction:
                    try:
                        user_num1 = float(input("Enter the first number: "))
                        user_num2 = float(input("Enter the second number: "))
                        print("The difference is ",
                              subtraction(user_num1, user_num2), ".\n", sep="")
                        run_subtraction = False
                    except ValueError:
                        print("That was not a valid input.")

            elif user_input == 3:  # division
                run_division = True
                while run_division:
                    try:
                        user_num1 = float(input("Enter a number: "))
                        user_num2 = float(input("Enter a second number: "))
                        division(user_num1, user_num2)
                        run_division = False
                    except ValueError:
                        print("That was not a valid input.")

            elif user_input == 4:  # multiplication
                run_multiplication = True
                while run_multiplication:
                    try:
                        user_num1 = float(input("Enter a number: "))
                        user_num2 = float(input("Enter a second number: "))
                        print("The product is ",
                              multiplication(user_num1, user_num2), ".\n",
                              sep="")
                    except ValueError:
                        print("That was not a valid input.")

            elif user_input == 5:  # calculates num1 to the num2 power
                run_exponents = True
                while run_exponents:
                    try:
                        user_num1 = float(input("Enter a number: "))
                        user_num2 = float(input("Enter a second number: "))
                        print(user_num1, " to the ", user_num2, " power is ",
                              exponents(user_num1, user_num2), ".\n", sep="")
                        run_exponents = False
                    except ValueError:
                        print("That was not a valid input.")

            elif user_input == 6:  # circle area
                run_circle_area = True
                while run_circle_area:
                    try:
                        user_radius = float(input("Enter a radius: "))
                        print("The area is ", circle_area(user_radius), ".\n",
                              sep="")
                        run_circle_area = False
                    except ValueError:
                        print("That was not a valid input.")

            elif user_input == 7:  # cube area
                run_cube_area = True
                while run_cube_area:
                    try:
                        user_length = float(
                            input("Enter the length of one side of the cube"))
                        print("The area of the cube is ",
                              cube_area(user_length), ".\n", sep="")
                        run_cube_area = False
                    except ValueError:
                        print("That was not a valid input.")

            elif user_input == 8:  # repeats given word a certain number of
                # times
                run_repeat = True
                while run_repeat:
                    try:
                        user_word = input(
                            "Enter the word you want to repeat: ")
                        repeat = int(
                            input("How many times do you want to repeat it: "))
                        print(user_word * repeat, "\n")
                        run_repeat = False
                    except ValueError:
                        print("That was not a valid input.")

            elif user_input == 9:  # whether num1 <,>, or = num2
                run_inequalities = True
                while run_inequalities:
                    try:
                        user_num1 = float(input("Enter a number: "))
                        user_num2 = float(input("Enter a second number: "))
                        inequalities(user_num1, user_num2)
                        run_inequalities = False
                    except ValueError:
                        print("That was not a valid input.")

            elif user_input == 10:  # whether a number is in a certain range
                run_range = True
                while run_range:
                    try:
                        user_num = float(input("Enter a number: "))
                        user_start_range = float(
                            input("What number does the range start at? "))
                        user_end_range = float(
                            input("What number does the range end at? "))
                        range_function(user_num, user_start_range,
                                       user_end_range)
                        run_range = False
                    except ValueError:
                        print("That was not a valid input.")

            elif user_input == 11:  # prints number of calculations performed
                # ran and stops running
                print("You ran the program", num_calculations, "times.")
                continue_program = False

        if user_input not in range(1, 12):
            print(
                "That was not an option. "
                "Please select an option from 1 to 11.")

        num_calculations += 1  # keeps count of the number of calculations
        # performed


if __name__ == "__main__":
    main()
