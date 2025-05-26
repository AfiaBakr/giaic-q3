def main():
    
    curr_value = int(input("Enter a number: "))

    # Double and print until curr_value is 100 or more
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value, end=" ")

if __name__ == "__main__":
    main()
