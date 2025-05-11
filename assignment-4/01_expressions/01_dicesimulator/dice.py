
# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.

"""
Program: dicesimulator
----------------------
Simulate rolling two dice, three times.  Prints
the results of each dice roll.  This program is used
to show how variable scope works.
"""

# Import the random library which lets us simulate random things like dice!
import random

# Number of sides on each dice to roll
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their total
    """
    dice1: int = random.randint(1, NUM_SIDES)
    dice2: int = random.randint(1, NUM_SIDES)
    total: int = dice1 + dice2
    print("Total of two dice:", total)

def main():
    dice1: int = 10
    print("dice1 in main() starts as: " + str(dice1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("dice1 in main() is: " + str(dice1))

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()