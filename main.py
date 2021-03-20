#Khushi Patel
#Calculator

import math

def welcome_message():
    print("Welcome to the calculator.")
    name = input("What is your name? ")
    print("Let's get started, " + name + "! ", end='\n\n')

def addition(num1, num2):
    sum = num1 + num2
    print("The sum is ", sum, ".\n", sep="")

def subtraction(num1, num2):
    difference = num1 - num2
    return difference

def division(num1, num2):
    choice = input("Would like \na) a quotient or \nb) the remainder and whole number?")
    #only returns the quotient as a decimal
    if choice == "a" or choice == "A":
        quotient = num1/num2
        print("The quotient is ", quotient, ".", sep="")
    #returns the integer portion of the quotient and the remainder
    elif choice == "B" or choice == "b":
        remainder = num1%num2
        print("The remainder is, ", remainder, ".", sep="")
        integer_portion = num1//num2
        print("Floor division: ", integer_portion, ".\n", sep="")

def multiplication(num1, num2):
    product = num1*num2
    return product

def exponents(num1, num2):
    product = num1**num2
    return product

def circle_area(radius):
    area = radius**2*math.pi
    return area

def cube_area(side_length):
    area = side_length**3
    return area

def inequalities(num1, num2):
    if num1 < num2:
        print(num1, " is less than ", num2, sep="")
    elif num1 == num2:
        print(num1, "is equal to ", num2, sep="")
    elif num1 > num2:
        print(num1, " is great than ", num2, sep="")
    else:
        print("Could not compute an inequality.")

def range_function(num, start_range, end_range):
    #checks to see if the number entered is in the range entered by user
    if num > start_range and num < end_range:
        print(num, "is in the range.\n")

def main():
    continue_program = True
    num_calculations = 0
    #all the calculation options in the program
    calculation_options =["addition", "subtraction", "division", "multiplication", "exponents", "circle area", "cube area",
                          "repeat words", "inequalities", "in-range", "stop program"]

    while continue_program != False:
        print("Enter the option number of the calculation you would like to perform: ")
        #prints the calculations options list as a numbered list
        for calculation in calculation_options:
            print(calculation_options.index(calculation)+1, ". ", calculation, sep="")

        user_input = int(input(""))

        if user_input in range(1,12):
            if user_input == 1: #addition
                user_num1 = float(input("Enter a number: "))
                user_num2 = float(input("Enter a second number: "))
                addition(user_num1, user_num2)

            elif user_input == 2: #subtraction
                user_num1 = float(input("Enter a number: "))
                user_num2 = float(input("Enter a second number: "))
                print("The difference is ", subtraction(user_num1, user_num2), ".\n", sep="")

            elif user_input == 3: #division
                user_num1 = float(input("Enter a number: "))
                user_num2 = float(input("Enter a second number: "))
                division(user_num1, user_num2)

            elif user_input == 4: #multiplication
                user_num1 = float(input("Enter a number: "))
                user_num2 = float(input("Enter a second number: "))
                print("The product is ", multiplication(user_num1, user_num2), ".\n", sep="")

            elif user_input == 5: #calculates num1 to the num2 power
                user_num1 = float(input("Enter a number: "))
                user_num2 = float(input("Enter a second number: "))
                print(user_num1, " to the ", user_num2, " power is ", exponents(user_num1, user_num2), ".\n", sep="")

            elif user_input == 6: #circle area
                user_radius = float(input("Enter a radius: "))
                print("The area is ", circle_area(user_radius), ".\n", sep="")

            elif user_input == 7: #cube area
                user_length = float(input("Enter the length of one side of the cube"))
                print("The area of the cube is ", cube_area(user_length), ".\n", sep="")

            elif user_input == 8: #repeats given word a certain number of times
                user_word = input("Enter the word you want to repeat: ")
                repeat = int(input("How many times do you want to repeat it: "))
                print(user_word*repeat, "\n")

            elif user_input == 9: #whether num1 <,>, or = num2
                user_num1 = float(input("Enter a number: "))
                user_num2 = float(input("Enter a second number: "))
                inequalities(user_num1, user_num2)

            elif user_input == 10: #whether a number is in a certain range
                user_num = float(input("Enter a number: "))
                user_start_range = float(input("What number does the range start at? "))
                user_end_range = float(input("What number does the range end at? "))
                range_function(user_num, user_start_range, user_end_range)

            elif user_input == 11: #prints number of calculations performed ran and stops running
                print("You ran the program", num_calculations, "times.")
                continue_program = False

        if user_input not in range(1,12):
            print("That was not an option.")

        num_calculations += 1 #keeps count of the number of calculations performed

main()