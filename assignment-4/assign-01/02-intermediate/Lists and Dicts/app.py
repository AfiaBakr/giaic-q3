def main():
    # Create a list called fruit_lst that contains the following fruits
    fruit_lst = ['apple', 'banana', 'orange', 'grape', 'pineapple']

    # Print the length of the list
    lst_length = len(fruit_lst)
    print("Length of the list:", lst_length)

    # Add 'mango' at the end of the list
    fruit_lst.append('mango')

    # Print the updated list
    print("Updated fruit list:")
    for fruit in fruit_lst:
        print(fruit)

if __name__ == "__main__":
    main()
