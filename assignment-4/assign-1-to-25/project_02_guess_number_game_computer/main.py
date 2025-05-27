import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess =int(input(f"Guess your number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, Your number is too low, guess again!")
        elif guess > random_number:
            print("Sorry, Your number is too high, guess again!")

    print(f"Yay! Congrats, you have the guess the {random_number} correctly.")

guess(10)