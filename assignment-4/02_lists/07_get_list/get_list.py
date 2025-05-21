def main():
    list = []  # Make an empty list to store things in

    value = input("Enter a value: ")  # Get an initial value
    while value:  # While the user input isn't an empty value
        list.append(value) # Add val to list
        value = input("Enter a value: ")  # Get the next value to add

    print("Here's the list:", list)


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()