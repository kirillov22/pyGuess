#!/usr/bin/python3
from random import *
import sys
LINE = "-" * 30


def print_instructions():
    """Void; Prints out the instructions when the program starts to run"""
    #
    # TODO: Add instructions to be printed
    print("Hmmm. So you think you want to take me on? I am an artificial intelligence "
          "greater than the likes of anything you have ever see before!")
    print()


def generate_random_num(num1, num2):
    """Integer; generates a random number in a specified range, default values are
    between 0 and 1000"""
    return randint(num1, num2)
    
    
def check_is_num(user_input):
    """Boolean; Checks whether the input is a number"""
    try:
        int(user_input)
        return True
    except ValueError:
        return False


def get_num_guesses():
    """Integer; gets the number of guesses that the user will have for the game"""
    num_guesses = input("How many guesses would you like? You can choose between 1 and 10: ").strip()
    check_terminate(num_guesses)

    is_valid = check_is_valid_num(num_guesses)
    if is_valid:
        if int(num_guesses) < 1 or int(num_guesses) > 10:
            is_valid = False

    while not is_valid:
        print("Looks like that number is not valid. Please enter one between 1 and 10.")
        num_guesses = input("How many guesses would you like? You can choose between 1 and 10: ").strip()
        is_valid = check_is_valid_num(num_guesses)

    return int(num_guesses)


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
    if not is_digit:
        return False
    elif is_digit and int(user_input) > 0:
        return True
    else:
        return False


def get_number(to_find):
    """Integer; Gets the user to input a number"""
    if to_find == "low":
        to_print0 = "Please enter a number for the LOWEST value to be: "
        to_print1 = "Please enter a number for the LOWEST value to be. Enter -1 to terminate: "
    elif to_find == "high":
        to_print0 = "Please enter a number for the HIGHEST value to be: "
        to_print1 = "Please enter a number for the HIGHEST value to be. Enter -1 to terminate: "

    num = input(to_print1).strip()

    # Check to terminate program
    check_terminate(num)

    # Check the input is actually a number
    is_num = check_is_num(num)
    while not is_num:
        print("You did not enter a correct number. Please try again!")
        num = input(to_print0).strip()
        is_num = check_is_num(num)

    # Checks that the number is valid. Needs to be a natural number where 0 is included
    is_valid = check_is_valid_num(num)

    while not is_valid:
        print("You did not enter a valid number. It needs to be a natural number.")
        num = input(to_print0).strip()
        is_valid = check_is_valid_num(num)

    return num


def end_procedures(is_winner, number):
    """Void; This runs at the end of the game and determines whether the player won or not"""
    if is_winner:
        print("Sigh... You have correctly guessed my number. It was {}.".format(number))
        print("I guess you have bested me. Humans have once again outwitted us machines")
    else:
        print(LINE)
        print("Hah! Looks like you're out of guesses....")
        print("I win! My number was {}. This game is too easy for the likes of me.".format(number))
        print("This is a true showing of why humans are inferior to the computer overlords!")

    sys.exit()


def main():
    """Starts to run the program"""
    # Initialise variables
    print_instructions()
    num_guesses = get_num_guesses()
    print("You will have {} guess to beat me! Good luck friend....".format(num_guesses))
    num1 = get_number("low")
    num2 = get_number("high")
    low_end = num1
    high_end = num2
    guess_num = 1
    is_game_ended = False

    number_to_guess = generate_random_num(int(num1), int(num2))
    print("Generating a random number from the range {} - {}....".format(num1, num2))

    while guess_num <= num_guesses and not is_game_ended:
        print(LINE)
        print("Guess number: {} ".format(guess_num))
        guess = input("Please enter your guess: ").strip()

        is_valid = check_is_valid_num(guess)
        while not is_valid:
            print("You did not enter a valid guess. Please try again!")
            guess = input("Please enter your guess: ").strip()
            is_valid = check_is_valid_num(guess)

        guess = int(guess)
        if guess == number_to_guess:
            print("What!??!?!?!?!?!??? How was I beaten? I am a superior artificial intelligence!")
            is_game_ended = True
        elif guess_num != num_guesses:
            if guess > number_to_guess:
                guess_direction = "LOWER"
                high_end = guess
            else:
                guess_direction = "HIGHER"
                low_end = guess
            print("Nope! That was not it. Try guessing {} this time.".format(guess_direction))
            print("Here is a hint: Try guessing between {} and {}".format(low_end, high_end))

        guess_num += 1

    end_procedures(is_game_ended, number_to_guess)


if __name__ == "__main__":    
    main()
