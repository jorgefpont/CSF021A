"""
Tests the Employee and Manager class
by creating a list of managers and employees
and using == and < to test the __eq__ and __lt__ methods
Also creates a new list ordered by last name
"""
from employee import Employee
from manager import Manager

employee1 = Employee("Mickey", "Mouse", "123-12-1234", 100000)
employee2 = Employee("Minnie", "Mice", "123-12-1235", 120000)
employee3 = Employee("Mickey", "Mouse", "555-12-1212", 100000)
mgr1 = Manager("Goofy", "Smith", "123-12-1236", 150000, "Director", 25000)
mgr2 = Manager("Speedy", "Gonzalez", "666-99-5555", 110000.00, "Sr. Director", 30000.00)

staffList = [employee1, employee2, employee3, mgr1, mgr2]

# name comparisons
print('Name equal / == comparisons\n')
print(employee1.last_name,',',employee1.first_name,'==',
      employee2.last_name,',',employee2.first_name)
print(employee1 == employee2)
print()
print(employee1.last_name,',',employee1.first_name,'==',
      mgr1.last_name,',', mgr1.first_name)
print(employee1 == mgr1)
print()
print(employee2.last_name,',',employee2.first_name,'==',
      mgr2.last_name,',', mgr2.first_name)
print(employee2 == mgr2)
print()
print(employee1.last_name,',',employee1.first_name,'==',
      employee3.last_name,',',employee3.first_name)
print(employee1 == employee3)
print()

print('Name less-than / < comparisons\n')
print(employee1.last_name,',',employee1.first_name,'<',
      employee2.last_name,',',employee2.first_name)
print(employee1 < employee2)
print()
print(employee1.last_name,',',employee1.first_name,'<',
      mgr1.last_name,',', mgr1.first_name)
print(employee1 < mgr1)
print()
print(employee2.last_name,',',employee2.first_name,'<',
      mgr2.last_name,',', mgr2.first_name)
print(employee2 < mgr2)
print()
print(mgr1.last_name,',',mgr1.first_name,'<',
      mgr2.last_name,',', mgr2.first_name)
print(mgr1 < mgr2)
print()

# Confirm that these two new methods are consistent with each other.
# For example, if a<b returns False and b<a returns False,
# then a==b must return True, for every possible value of a and b.
# Test next:
print('Test that if (a<b & b<a) False then a==b True')
print(employee1 < employee3)
print(employee3 < employee1)
print(employee1 == employee3)
print()

# list ordering
print('Names in un-ordered list')
for staff in staffList:
    print(staff.last_name, ',',staff.first_name)

print()
print('Names is ordered list')
sortedStaffList = sorted(staffList)
for staff in sortedStaffList:
    print(staff.last_name, ',',staff.first_name)

"""
/home/jorge/csf021aWork/bin/python /home/jorge/csf021a/csf021aWork/employeelTest_hwk8.py
Name equal / == comparisons

Mouse , Mickey == Mice , Minnie
False

Mouse , Mickey == Smith , Goofy
False

Mice , Minnie == Gonzalez , Speedy
False

Mouse , Mickey == Mouse , Mickey
True

Name less-than / < comparisons

Mouse , Mickey < Mice , Minnie
False

Mouse , Mickey < Smith , Goofy
True

Mice , Minnie < Gonzalez , Speedy
False

Smith , Goofy < Gonzalez , Speedy
False

Test that if (a<b & b<a) False then a==b True
False
False
True

Names in un-ordered list
Mouse , Mickey
Mice , Minnie
Mouse , Mickey
Smith , Goofy
Gonzalez , Speedy

Names is ordered list
Gonzalez , Speedy
Mice , Minnie
Mouse , Mickey
Mouse , Mickey
Smith , Goofy

Process finished with exit code 0

"""
