from employee import Employee

class Manager (Employee):
    """ One object of class Manager represents one special class of
    employee who is a manager """

    def __init__(self, first_name='', last_name='', ssn='', salary=0.0,
                 title = '', bonus = 0.0):
        """initialize manager object"""

        self.first_name = first_name
        self.last_name = last_name
        self.ssn = ssn
        self.salary = salary

        Employee.__init__(self, first_name, last_name, ssn, salary)
        # calls the Account constructor to initialize that part of the object

        self.title = title
        self.bonus = bonus

    def __str__(self):
        """ print manager object"""
        return Employee.__str__(self) + "%s\n%.2f\n" % (self.title,
            self.bonus)

""" This is the test program to see how these two types of objects are constructed """

if __name__ == "__main__":
    mgr1 = Manager("Goofy", "Smith", "123-12-1236", 150000, "Director", 25000)
    print (mgr1)
    mgr1.giveRaise(25)
    print(mgr1)

"""
/home/jorge/csf021aWork/bin/python /home/jorge/csf021a/csf021aWork/module7/payrollTest.py
pre-raise payroll:

Mickey Mouse
123-12-1234
100000.00

Minnie Mouse
123-12-1235
120000.00

Goofy Smith
123-12-1236
150000.00
Director
25000.00

post raise payroll:

Mickey Mouse
123-12-1234
125000.00

Minnie Mouse
123-12-1235
150000.00

Goofy Smith
123-12-1236
187500.00
Director
25000.00


Process finished with exit code 0
"""