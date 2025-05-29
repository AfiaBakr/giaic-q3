PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48

def main():
    # Get the user's age
    user_age = int(input("How old are you? "))

    # Check if the user can vote in Peturksbouipo
    if user_age >= PETURKSBOUIPO_AGE:
        print(f"You can vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE} ")
    else:
        print(f"You cannot vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE} ")
    
    # Check if the user can vote in Stanlau
    if user_age >= STANLAU_AGE:
        print(f"You can vote in Stanlau where the voting age is {STANLAU_AGE}")
    else:
        print(f"You cannot vote in Stanlau where the voting age is {STANLAU_AGE} ")
    
    # Check if user can vote in Mayengua
    if user_age >= MAYENGUA_AGE:
        print(f"You can vote in Mayengua where the voting age is {MAYENGUA_AGE} ")
    else:
        print(f"You cannot vote in Mayengua where the voting age is {MAYENGUA_AGE}")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()