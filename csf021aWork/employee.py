"""Defines class Employee and its methods"""

class Employee:
    """ One object of class Employee represents one Employee """

    def __init__(self):
        """Employee constructor"""
        self.first_name = ''
        self.last_name = ''
        self.ssn = ''
        self.salary = 0.0

    def setData(self, first_name, last_name, ssn, salary):
        """Set emloyee data"""
        self.first_name = first_name
        self.last_name = last_name
        self.ssn = ssn
        self.salary = salary

    def __str__(self):
        """Returns a string containing the data in Employee"""
        return "%s %s\n%s\n%.2f\n" % (self.first_name,
                                      self.last_name,
                                      self.ssn,
                                      self.salary)

    def giveRaise(self, percentRaise):
        """Returns new salary after raise"""
        self.salary = self.salary * (1 + (percentRaise / 100))

    def __eq__(self, other):
        """Returns True if self == other, False otherwise"""
        if self.first_name.lower() == other.first_name.lower() and \
                self.last_name.lower() == other.last_name.lower():
            return True
        else:
            return False

    def __lt__(self, other):
      """
      Returns True when the name in self is alphabetically less than
      the name in other, and False otherwise.
      If the last names are equal, checks the first names
      to determine which object is less than the other.
      Method is case insensitive
      """
        # compare last names
        if self.last_name.lower() < other.last_name.lower():
            return True

        # if last names are equal, first name comparison case 1
        elif self.last_name.lower() == other.last_name.lower() and \
                self.first_name.lower() < other.first_name.lower():
            return True

        # if last names are equal, first name comparison case 2
        elif self.last_name.lower() == other.last_name.lower() and \
                self.first_name.lower() > other.first_name.lower():
            return False

        # both first and last names are the same or
        # self.last_name > other.last_name
        else:
            return False


if __name__ == "__main__":
    """Test the class"""
    employee1 = Employee()
    employee1.setData("Mickey", "Mouse", "123-12-1234", 100000)
    employee2 = Employee()
    employee2.setData("Minnie", "Mouse", "123-12-1235", 120000)
    employee3 = Employee()
    employee3.setData("Mickey", "Mouse", "555-12-1212", 100000)
    employee4 = Employee()
    employee4.setData("Mickey", "Smith", "555-12-1212", 100000)

    print(employee1)
    print(employee2)
    print(employee3)
    print()
    employee1.giveRaise(25)
    print(employee1)
    print()
    print(employee1 == employee2)
    print(employee1 == employee3)
    print(employee1 == employee4)
    print()
    print(employee1 < employee2)
    print(employee1 < employee3)
    print(employee1 < employee4)
