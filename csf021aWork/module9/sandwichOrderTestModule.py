"""
Tests for Sandwich and Order classes.
Test for file witing.
"""

from order import Order
from sandwich import Sandwich

# create Sandwich objects
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

# create 1 Order object
# print and get the proce for the order
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

