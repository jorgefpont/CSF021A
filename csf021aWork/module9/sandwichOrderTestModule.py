"""
Tests for Sandwich and Order classes.
Test for writing the order object to a binary file.
"""

from order import Order
from sandwich import Sandwich
import pickle

# create Sandwich objects
s1 = Sandwich("Joe")
s1.setBread("wheat")
s1.setMeat("steak")
s1.addCondiment("Lettuce")

s2 = Sandwich("Mary")
s2.setBread("white")
s2.setCheese("cheddar")
s2.addCondiment("Mayo")

s3 = Sandwich("Elizabeth")
s3.setBread("sourdough")
s3.setMeat("ham")
s3.setCheese("swiss")
s3.addCondiment("mayo")
s3.addCondiment("mustard")
s3.setToasted(True)

s4 = Sandwich("Bennie")
s4.setBread("wheat")
s4.setCheese("Cheddar")
s4.setMeat("turkey")
s4.addCondiment("mustard")
s4.addCondiment("lettuce")
s4.setToasted(True)

s5 = Sandwich("Joe")
s5.setBread("pumpkin")
s5.setMeat("turkey")
s5.addCondiment("mayo")
s5.setToasted(False)

# create 2 Order objects
# print orders and price for the orders
print('\norder1:')
order1 = Order()
order1.addSandwich(s1)
order1.addSandwich(s2)
order1.addSandwich(s3)
print(order1)
print(order1.price())

print('\norder2:')
order2 = Order()
order2.addSandwich(s4)
order2.addSandwich(s5)
print(order2)
print(order2.price())

# demonstrate that modifying one of those Order objects
# does not effect the other Order object
# modify order2 by adding another sandwich
print('\nmodified order2 and original order 1 (to make sure order1 not modified):')
order2.addSandwich(s2)
print(order2)
print(order2.price())
# check that order1 object has not been modified
print(order1)
print(order1.price())

# test binary file write and read
print('\nTest writing and reading order1 to a binary file')
datafile = open('orderFile.pkl', 'wb')
pickle.dump(order1, datafile)
datafile.close()

datafile = open('orderFile.pkl', 'rb')
copyOfOrder1 = pickle.load(datafile)
print()
print("\nCopy of order1 from binary file:")
print(copyOfOrder1)
print(copyOfOrder1.price())   # check the price just in case

"""
/home/jorge/venv/bin/python /home/jorge/csf021a/CSF021A/csf021aWork/module9/sandwichOrderTestModule.py

order1:

Joe: wheat, steak, ['Lettuce'], not toasted
Mary: white, cheddar, ['Mayo'], not toasted
Elizabeth: sourdough, swiss, ham, ['mayo', 'mustard'], toasted
16.0

order2:

Bennie: wheat, Cheddar, turkey, ['mustard', 'lettuce'], toasted
Joe: pumpkin, turkey, ['mayo'], not toasted
11.5

modified order2 and original order 1 (to make sure order1 not modified):

Bennie: wheat, Cheddar, turkey, ['mustard', 'lettuce'], toasted
Joe: pumpkin, turkey, ['mayo'], not toasted
Mary: white, cheddar, ['Mayo'], not toasted
16.0

Joe: wheat, steak, ['Lettuce'], not toasted
Mary: white, cheddar, ['Mayo'], not toasted
Elizabeth: sourdough, swiss, ham, ['mayo', 'mustard'], toasted
16.0

Test writing and reading order1 to a binary file


Copy of order1 from binary file:

Joe: wheat, steak, ['Lettuce'], not toasted
Mary: white, cheddar, ['Mayo'], not toasted
Elizabeth: sourdough, swiss, ham, ['mayo', 'mustard'], toasted
16.0

Process finished with exit code 0

"""

