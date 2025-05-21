
# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

def main():
    
    num1 : str = input("Enter first number: ")
    num1 : int = int(num1)
    num2  : str = input("Enter second number: ")
    num2 : int = int(num2)
    total : int = num1 + num2
    print(f"The total is " + str(total) + ".")

if __name__ == '__main__':
    main()

