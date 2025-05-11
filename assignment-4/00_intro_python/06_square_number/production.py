
# Ask the user for a number and print its square (the product of the number times itself).

# Here's a sample run of the program (user input is in bold italics):

# Type a number to see its square: 4

# 4.0 squared is 16.0


def main():
    # ANSI escape codes: \033[1m = bold, \033[3m = italic, \033[0m = reset
    num: float = float(input("\033[1m\033[3mType a number to see its square: \033[0m")) # Make sure to cast the input to a float so we can do math with it!
    print(str(num) + " squared is " + str(num ** 2)) # num * num is equivalent to num ** 2. The ** operator raises something to a power!


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
