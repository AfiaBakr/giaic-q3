# 10. Instance Methods
# Assignment:
# Create a class Dog with instance variables name and breed. 
# Add an instance method bark() that prints a message including the dog's name.


class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed      # instance variables

    def bark(self):             # instance method
        print(f"{self.name}, {self.breed} is barking .. ")

if __name__ == "__main__":
    my_dog = Dog("My Dog","German Shepherd")
    my_dog.bark()
    
