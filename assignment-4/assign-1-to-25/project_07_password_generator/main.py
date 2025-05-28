import random

print("Welcome to Password Genetator..")

chars = 'asdfghjkl;zxcvbnm,./qwertyuiop!@#$%^&*+_-=1234567890?><()[{ASDCEWXZQFRVBGTYHNMJUIKLOP'

number = input('Enter a number to generate the password:  ')
number = int(number)

lenght = input("Your password lenght:  ")
lenght = int(lenght)

print("\nHere are your Passwords:")

for pwd in range(number):
    paswords = ' '
    for c in range(lenght):
        paswords += random.choice(chars)
    print(paswords)