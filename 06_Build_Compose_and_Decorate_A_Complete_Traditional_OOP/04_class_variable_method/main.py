# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. 
# Add a class method change_bank_name(cls, name) that allows changing the bank name. 
# Show that it affects all instances.

class Bank():
    bank_name = "ABC Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

if __name__ =="__main__":
    user1 = Bank()
    user2 = Bank()

    print("Before changing Bank Name:")
    print(f"User 1 bank name {user1.bank_name}")
    print(f"User 2 bank name {user2.bank_name}")
    
    Bank.change_bank_name("XYZ Bank")

    print("\nAfter changing Bank Name:")
    print(f"User 1 bank name {user1.bank_name}")
    print(f"User 2 bank name {user2.bank_name}")
    
