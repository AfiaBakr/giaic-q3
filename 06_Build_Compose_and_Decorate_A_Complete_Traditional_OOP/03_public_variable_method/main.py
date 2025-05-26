# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). 
# Instantiate the class and access both from outside the class.

class Car():
    def __init__(self, brand):
        self.brand = brand


    def start(self):
        print(f"The {self.brand} is comming now.....")


if __name__ =="__main__":
    my_car =Car("Toyota")
    my_car.start()
    print("Outside the class: ",my_car.brand)