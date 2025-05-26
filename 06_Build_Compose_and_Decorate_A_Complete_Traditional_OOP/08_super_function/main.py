# 8. The super() Function
# Assignment:
# Create a class Person with a constructor that sets the name. 
# Inherit a class Teacher from it, add a subject field, 
# and use super() to call the base class constructor.


# parent class
class Person:
    def __init__(self, name):
        self.name = name

# child class
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

# display
    def display(self):
        print(f"Teacher's name :{self.name} and Teacher's name : {self.subject}")

if __name__ =="__main__":
   
    techer1 = Teacher("Alia", "English")
    techer1.display()
    #or
    print("\nTeacher's name :", techer1.name)
    print("Teacher's subject :", techer1.subject)