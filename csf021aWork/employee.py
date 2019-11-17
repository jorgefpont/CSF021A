class Employee:
   """ One object of class Employee represents one Employee """

   def __init__(self, first_name='', last_name='', ssn='', salary=0.0):

      self.first_name = first_name
      self.last_name = last_name
      self.ssn = ssn
      self.salary = salary

   def __str__(self):
      """
      Returns a string containing the data in Employee
      """
      return "%s %s\n%s\n%.2f\n" % (self.first_name,
                                   self.last_name,
                                   self.ssn,
                                   self.salary)

   def giveRaise(self, percentRaise):
      """
      Returns new salary after raise
      """
      self.salary = self.salary * (1 + (percentRaise/100))

   def __eq__(self, other):
      """
      Returns True if self == other, False otherwise
      """
      if self.first_name.lower() == other.first_name.lower() and \
      self.last_name.lower() == other.last_name.lower():
         return True
      else:
         return False

   def __lt__(self, other):
      """
      Return True when the name in self is alphabetically less than
      the name in other, and return False otherwise.
      If the last names are equal,checks the first names
      to determine which object is less than the other.
      Method is "case insensitive",
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
         return Fase

      # both first and last names are the same or
      # self.last_name > other.last_name
      else:
         return False
      

if __name__ == "__main__":
   """prints employee data"""
   employee1 = Employee("Mickey", "Mouse", "123-12-1234", 100000)
   employee2 = Employee("Minnie", "Mouse", "123-12-1235", 120000)
   employee3 = Employee("Mickey", "Mouse", "555-12-1212", 100000)
   employee4 = Employee("Mickey", "Smith", "555-12-1212", 100000)

   print(employee1)
   print(employee2)   
   print(employee3)
   employee1.giveRaise(25)
   print(employee1)

   print(employee1 == employee2)
   print(employee1 == employee3)
   print(employee1 == employee4)
   print()
   print(employee1 < employee2)
   #print(employee1 > employee2)
   print(employee1 < employee3)
   print(employee1 < employee4)
