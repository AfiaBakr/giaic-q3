# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. 
# Use a class variable and a class method with cls to manage and display the count.

class Counter():
    count = 0

    def __init__(self):
        Counter.count +=1

    @classmethod
    def Show_count(cls):
        print(f" Total number of Objects created: {cls.count}")

if __name__ =="__main__":
    obj1 = Counter()
    obj2 = Counter()
    obj3 = Counter()
    obj4 = Counter()
    obj5 = Counter()
    obj6 = Counter()
    Counter.Show_count()