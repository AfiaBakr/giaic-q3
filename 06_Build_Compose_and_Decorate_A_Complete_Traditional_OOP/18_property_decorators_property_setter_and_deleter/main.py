# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. 
# Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.


class Product():
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        """Getter for price"""
        return self.__price
    
    @price.setter
    def price(self, new_price):
        if not isinstance(new_price, int):
            raise ValueError("Name must be a intiger!")
        self.__price = new_price


    @price.deleter
    def price(self):
        print("Deleting price!")
        del self.__price


# Usage
p = Product(5000)
print(p.price)

# Getter
p.price = 6000
print(p.price)

# Deleter
p.price
# print(p.price)
# Now trying to print p.price will raise an error because it's deleted