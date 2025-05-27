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

def computer_guess(x):
    low = 1
    high = x
    feed_back = ''
    while feed_back != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feed_back = input(f"Is {guess} to high (H), too low (L), or correct (C)??").lower()
        if feed_back == 'h':
            high = guess - 1
        elif feed_back == 'l':
            low = guess + 1

    print(f"Yay! The computer guess your number, {guess}, correctly!.")


computer_guess(10)