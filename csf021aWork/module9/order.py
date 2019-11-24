"""
Defines class Order, in file contact.py
"""

from sandwich import Sandwich

class Order:
    """
    One object of class Order stores a number of Sandwich objects
    """
    def __init__(self):
        """
        initializes a new Order object
        """
        self.orderList = []

    def addSandwich(self, newSandwich):
        """
        adds newSandwich to the Order
        """
        self.orderList.append(newSandwich)

    def price(self):
        orderTotal = 0
        for item in self.orderList:
            orderTotal = orderTotal + item.getPrice()
        return orderTotal

    def __str__(self):
        """
        returns a string containing all the sandwiches in the Order
        """
        returnedString = ""
        for item in self.orderList:
            returnedString = returnedString + "\n" + str(item)
        return returnedString

# tests class Order

if __name__ == "__main__":
    s1 = Sandwich("Joe")
    s1.setMeat("steak")
    s1.addCondiment("Lettuce")
    print(s1)
    print(s1.getPrice())

    s2 = Sandwich("Mary")
    s2.setCheese("cheddar")
    s2.addCondiment("Mayo")
    print(s2)
    print(s2.getPrice())


    s3 = Sandwich("Elizabeth")
    s3.setBread("sourdough")
    s3.setMeat("ham")
    s3.setCheese("swiss")
    s3.addCondiment("mayo")
    s3.addCondiment("mustard")
    s3.setToasted(True)
    print(s3)
    print(s3.getPrice())

    order = Order()
    print(order)
    order.addSandwich(s1)
    print(order)
    print(order.price())
    order.addSandwich(s2)
    print(order)
    print(order.price())
    order.addSandwich(s3)
    print(order)
    print(order.price())
