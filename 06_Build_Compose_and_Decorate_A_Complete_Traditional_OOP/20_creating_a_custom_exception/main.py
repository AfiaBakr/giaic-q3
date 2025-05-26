# 20. Creating a Custom Exception
# Assignment:
# Create a custom exception InvalidAgeError.
# Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.



class InvalidAgeError(Exception):
    """Custom exception for invalid age (less than 18)."""
    pass


def check_age(age):
    if age < 18:
        raise InvalidAgeError("❌ Age must be at least 18.")
    else:
        print("✅ Age is valid.")


try:
    age_input = int(input("Enter your age: "))
    check_age(age_input)
except InvalidAgeError as e:
    print(e)
except ValueError:
    print("⚠️ Please enter a valid integer.")
