#!/usr/bin/env python3
from random import *
import sys


def print_instructions():
    """Void; Prints out the instructions when the program starts to run"""
    #
    # TODO: Add instructions to be printed


def generate_random_num(num1, num2):
    """Int; generates a random number in a specified range, default values are 
    between 0 and 1000"""
    return randint(num1, num2)


def check_guess(guess):
    """Boolean; Checks the guess to match the number that needs to be guessed. 
    Returns true is the nunber is correct"""
    #
    # TODO: Add method to check if the number is guessed
    
    
def check_is_num(user_input):
    """Boolean; Checks whether the input is a number"""
    if user_input.isdigit:
        return True
    else:
        return False


def get_num_guesses():
    """Integer; gets the number of guesses that the user will have for the game"""
    num_guesses = input("How many guesses would you like? You can choose between 1 and 10")
    check_terminate(num_guesses)

    is_valid = check_is_valid_num(num_guesses)
    while not is_valid:
        print("Looks like that number is not valid")


def check_terminate(user_input):
    """Boolean; Checks whether the input is -1 and if it is, the 
    program terminates"""
    if user_input == "-1":
        print("Goodbye friend and good luck!")
        sys.exit()
    else:
        pass
    
    
def check_is_valid_num(user_input):
    """Boolean; Checks whether the input is non-negative"""
    is_digit = check_is_num(user_input)
    if int(user_input) >= 0 and is_digit:
        return True
    else:
        return False


def get_number(to_find):
    """Integer; Gets the user to input a number"""
    if to_find == "low":
        to_print0 = "Please enter a number for the lowest value to be: "
        to_print1 = "Please enter a number for the lowest value to be. Enter -1 to terminate: "
    elif to_find == "high":
        to_print0 = "Please enter a number for the highest value to be: "
        to_print1 = "Please enter a number for the highest value to be. Enter -1 to terminate: "

    num = input(to_print1).strip()

    # Check to terminate program
    check_terminate(num)

    # Check the input is actually a number
    is_num = check_is_num(num)
    while not is_num:
        print("You did not enter a correct number. Please try again!")
        num = input(to_print0)
        is_num = check_is_num(num)

    # Checks that the number is valid. Needs to be a natural number where 0 is included
    is_valid = check_is_valid_num(num)

    while not is_valid:
        print("You did not enter a valid number. It needs to be a natural number.")
        num = input(to_print0)
        is_valid = check_is_valid_num(num)

    return num


def main():
    """Starts to run the program"""
    # Initialise variables
    num1 = get_number("low")
    num2 = get_number("high")
    LINE = "-"*30
    guess_num = 1

    number_to_guess = generate_random_num(int(num1), int(num2))
    print("Generating a random number from the range {} - {}....".format(num1, num2))
    print(number_to_guess)

    while guess_num:
        print(LINE)
        print("Guess number: {} ".format(guess_num))
        guess = input("Please enter your guess: ")

        is_valid = check_is_valid_num(guess)
        while not is_valid:
            print("You did not enter a valid guess. Please try again!")
            guess = input("Please enter your guess: ")
            is_valid = check_is_valid_num(guess)

        guess = int(guess)
        if check_guess(guess):
            print("Wow! You guessed this correctly. The number was {}.".format(number_to_guess))
        elif guess_num :
            if guess > number_to_guess:
                guess_direction = "LOWER"
            else:
                guess_direction = "HIGHER"
            print("Nope! That was not it. Try guessing {} this time.".format(guess_direction))
            # guess_num += 1

    print(LINE)
    print("Hah! Looks like you're out of guesses....")
    print("I win xD")
    print("This is a true showing of why humans are inferior to the computer overlords!")

if __name__ == "__main__":    
    main()
