# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:
    # a public variable name,
    # a protected variable _salary, and
    # a private variable __ssn.
# Try accessing all three variables from an object of the class and document what happens.

class Employee():
    def __init__(self, name, salary, ssn):
        self.name = name                            # public variable
        self._salary = salary                       # protected variable
        self.__ssn = ssn      # private variable

if __name__ =="__main__":
    employee = Employee("Aftab", 2500,  "123-45-6789")
    print("Public variable: ", employee.name)
    print("Protected variable: ", employee._salary)
    try:
        print("Private variable: ", employee.__ssn)
    except AttributeError:
        print("Cannot access private variable __ssn")