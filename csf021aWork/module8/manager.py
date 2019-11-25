"""Defines class Managers -- a sub-class of class Employee
 and its methods"""

from employee import Employee

class Manager (Employee):
    """ One object of class Manager represents one special class of
    employee who is also a manager """

    def __init__(self, first_name='', last_name='', ssn='', salary='',
                 title='', bonus=0.0):

        """initialize manager object"""
        Employee.__init__(self, first_name, last_name, ssn, salary)

        self.title = title
        self.bonus = bonus

    def __str__(self):
        """ print manager object"""
        return Employee.__str__(self) + "%s\n%.2f\n" % (self.title,
            self.bonus)

if __name__ == "__main__":
    """ This is the test program to see how these two types of objects are constructed """
    mgr1 = Manager("Goofy", "Smith", "123-12-1236", 150000, "Director", 25000)
    print (mgr1)
    mgr1.giveRaise(25)
    print(mgr1)

