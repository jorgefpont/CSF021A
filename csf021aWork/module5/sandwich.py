"""
Defines class Sandwich and tests it by creating sandwich objects.
The class has methods for specifying items added to the sandwich,
and for specifying the type of bread and whether the bread
should be toasted or not. The class has a method to calculate
the proce of the sandwich.
"""


class Sandwich:
    ''' One object of this class represents a sandwich
    with its ingredients'''

    def __init__(self, name):
        '''Initializes a single new Sandwich object by
        storing the name of the customer as its instance variable name.
        Assigns the initial value of None to all of the other instance variables'''
        self.name = name
        self.bread = None
        self.cheese = None
        self.meat = None
        self.condiments = None
        self.toasted = False

    def setBread(self, breadName):
        '''Sets the type of bread instance variable'''
        self.bread = breadName

    def setCheese(self, cheeseName):
        '''Sets the type of cheese instance variable'''
        self.cheese = cheeseName

    def setMeat(self, meatName):
        '''Sets the type of meat instance variable'''
        self.meat = meatName

    def addCondiment(self, additionalCondiment):
        '''Adds "additionalCondiment" to the list of condiments
        stored in the instance variable for the condiments list'''

        if self.condiments == None:
            self.condiments = [additionalCondiment]
        elif self.condiments != None:
            self.condiments.append(additionalCondiment)

    def setToasted(self, isToasted):
        '''Sets the toasted instance variable to be True
        if the parameter "isToasted" is True, False otherwise'''
        self.toasted = isToasted

    def getPrice(self):
        '''Returns the price of the sandwich based on the following:
        - Basic cheese sandwich with one condiment = $4.50
        - Meat added to the cheese sandwich + $1.00
        - Each additional condiment after the first + $0.50'''

        price = 4.5
        if self.meat is not None:
            price = price + 1.0
        if self.condiments is not None:
            numCondiments = len(self.condiments)
            price = price + 0.5 * (numCondiments - 1)
        return price

    def __str__(self):
        '''Returns a string containing the description of the sandwich
        which includes customer name, a list of all the ingredients,
        and whether the sandwich is toasted or not'''

        # example:
        # Bernie: wheat, Cheddar, turkey, ['mayo', 'mustard', 'lettuce'], not toasted
        # add 'toast' as a local variable for proper printing

        if self.toasted == True:
            toast = 'toasted'
        elif self.toasted == False:
            toast = 'not toasted'
        elif self.toasted == None:
            toast = None

        # Need to remove any None's from the sting
        # I don't know how ... si I came uo with a
        # bit of a complicated way -- it works

        sandwichList = [self.bread, self.cheese, self.meat, self.condiments]
        modSandwich = []  # remove Nones
        for i in sandwichList:
            if i != None:
                modSandwich.append(i)

        n2st = ''  # create new sub0string without the Nones
        for i in modSandwich:
            if type(i) is not list:
                n2st = n2st + i + ', '
            elif type(i) is list:
                n2st = n2st + str(i) + ', '

        # assemble output string
        sandwichOrder = f"{self.name}: {n2st}{toast}"
        return sandwichOrder


if __name__ == "__main__":
    ''' test function, makes several sandwich objects'''
    s = Sandwich("Bennie")
    print(s)
    s.setBread("wheat")
    print(s)
    s.setCheese("Cheddar")
    print(s)
    s.setMeat("turkey")
    print(s)
    s.addCondiment("mayo")
    print(s)
    s.addCondiment("mustard")
    print(s)
    s.addCondiment("lettuce")
    print(s)
    s.setToasted(True)
    print(s)
    print(s.getPrice())
    #
    s2 = Sandwich("Elizabeth")
    s2.setBread("sourdough")
    s2.setCheese("swiss")
    s2.addCondiment("mayo")
    s2.addCondiment("mustard")
    s2.setToasted(True)
    print(s2)
    print(s2.getPrice())

"""
/home/jorge/csf021aWork/bin/python /home/jorge/csf021a/csf021aWork/module5/sandwich.py
Bennie: not toasted
Bennie: wheat, not toasted
Bennie: wheat, Cheddar, not toasted
Bennie: wheat, Cheddar, turkey, not toasted
Bennie: wheat, Cheddar, turkey, ['mayo'], not toasted
Bennie: wheat, Cheddar, turkey, ['mayo', 'mustard'], not toasted
Bennie: wheat, Cheddar, turkey, ['mayo', 'mustard', 'lettuce'], not toasted
Bennie: wheat, Cheddar, turkey, ['mayo', 'mustard', 'lettuce'], toasted
6.5
Elizabeth: sourdough, swiss, ['mayo', 'mustard'], toasted
5.0

Process finished with exit code 0
"""