
# Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

# Here's a sample run of the program (user input is in bold italics - note the space between the prompt and the user input!):

# What's your favorite animal? cow

# My favorite animal is also cow!


def main():
    # ANSI escape codes: \033[1m = bold, \033[3m = italic, \033[0m = reset
    favorate_animal :str =input('\033[1m\033[3mWhat is your favorite animal? \033[0m')

    print(f"Your favorate animal is {favorate_animal}")
    print("My favorite animal is also cow!")

if __name__ == '__main__':
    main()