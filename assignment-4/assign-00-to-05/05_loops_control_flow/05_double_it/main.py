# Ask the user to enter a number
curr_value = int(input("Enter a number: "))

# Double the number until it reaches or exceeds 100
while curr_value < 100:
    curr_value = curr_value * 2
    print(curr_value, end=' ')
