#!/usr/bin/env python3
from random import *
from sys import *

def print_instructions():
    """Void; Prints out the instructions when the program starts to run"""
    #
    #TODO: Add instructions to be printed


def generate_random_num(num1, num2):
    """Int; generates a random number in a specified range, default values are 
    between 0 and 1000"""
    return randint(num1,num2)


def check_guess(guess):
    """Boolean; Checks the guess to match the number that needs to be guessed. 
    Returns true is the nubmer is correct"""
    #
    #TODO: Add method to check if the number is guessed
    
    
def check_is_num(user_input):
    """Boolean; Checks whether the input is a number"""
    if user_input.isdigit:
        return True
    else:
        return False
    
    
def check_terminate(user_input):
    """Boolean; Checks whether the input is -1 and if it is, the 
    program terminates"""
    if user_input == int(-1):
        return True
    else:
        return False
    
    
def check_is_valid_num(user_input):
    """Boolean; Checks whether the input is non-negative"""
    if int(user_input) >= 0:
        return True
    else:
        return False


def main():
    """Starts to run the program"""
    #Initialise variables
    num1 = 0
    num2 = 1000
    num1 = input("Please enter a number for the lowest value to be. Enter -1 to terminate: ")
    
    #Check the input is actually a number
    is_num = check_is_num(num1)
    
    #Check to terminate program
    if check_terminate(num1):
        print("Goodbye friend and goodluck!")
        system.exit()
    
    #Checks that the number is valid. Needs to be a natural number where 0 is included    
    is_valid = check_is_valid_num(num1)
    
    #While an incorrect input is given, keep asking until a valid one is given
    # or until the program is told to terminate
    ##TODO: Refactor this to have it also check the second number
    while is_valid == False:
        num1 = input("Please enter a number for the lowest value to be: ")
        is_num = check(num1)
        if check_terminate(num1):
            print("Goodbye friend and goodluck!")
            system.exit()
        is_valid = check_is_valid_num(num1)
        
        
    
        
    number_to_guess = generate_random_num(int(num1), int(num2))
        
    print(number_to_guess)
        
if __name__ == "__main__":    
    main()