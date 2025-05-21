def get_last_element(list):
    """
    Prints the first element of a provided list.
    """

    print(list[len(list) - 1])

    print(list[-1])

# There is no need to edit code beyond this point

def get_list():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    list = []
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        list.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return list

def main():
    list = get_list()
    get_last_element(list)


if __name__ == '__main__':
    main()
