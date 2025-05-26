# 19. callable() and __call__()
# Assignment:
# Create a class Multiplier with an __init__() to set a factor. 
# Define a __call__() method that multiplies an input by the factor. 
# Test it with callable() and by calling the object like a function.


class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor


# Create an instance with a factor of 3
triple = Multiplier(3)

# ✅ Test with callable()
print(callable(triple))  # Output: True

# ✅ Call the object like a function
result = triple(10)      # 10 * 3 = 30
print(result)            # Output: 30
