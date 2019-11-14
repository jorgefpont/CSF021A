class Employee:
   """ One object of class Employee represents one Employee """

   def __init__(self, first_name='', last_name='', ssn='', salary=0.0):

      self.first_name = first_name
      self.last_name = last_name
      self.ssn = ssn
      self.salary = salary

   def __str__(self):
      """
      returns a string containing the data in Employee
      """
      return "%s %s\n%s\n%.2f\n" % (self.first_name,
                                   self.last_name,
                                   self.ssn,
                                   self.salary)

   def giveRaise(self, percentRaise):
      self.salary = self.salary * (1 + (percentRaise/100))

if __name__ == "__main__":
   """prints employee data"""
   employee1 = Employee("Mickey", "Mouse", "123-12-1234", 100000)
   employee2 = Employee("Minnie", "Mouse", "123-12-1235", 120000)

   print(employee1)
   print(employee2)
   employee1.giveRaise(25)
   print(employee1)
