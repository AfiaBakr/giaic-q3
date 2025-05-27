
import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while '_' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    while len(word_letters) > 0:
        # show current used letters
        print("You have used these letters: ", ' '.join(used_letters))

        # show current word
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("Current word: ", ' '.join(word_list))

        # get user input
        user_letter = input("Guess your letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("Correct!")
            else:
                print("Letter is not in the word.")

        elif user_letter in used_letters:
            print("You have already used that letter. Please try again.")

        else:
            print("Invalid character. Please try again.")

    print(f"Yay! You guessed the word: {word}!")


hangman()
