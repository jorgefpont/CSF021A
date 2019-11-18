from employee import Employee
from manager import Manager

employee1 = Employee("Mickey", "Mouse", "123-12-1234", 100000)
employee2 = Employee("Minnie", "Mouse", "123-12-1235", 120000)
mgr1 = Manager("Goofy", "Smith", "123-12-1236", 150000, "Director", 25000)

staffList = [employee1, employee2, mgr1]

# print the pre-raise staff list
print("pre-raise payroll:\n")
for staff in staffList:
    print(staff)

# give raise to everyone in the staff
for staff in staffList:
    staff.giveRaise(25)
    # everyone gets a 25% raise!!!

# check that everyone got their raise
print("post raise payroll:\n")
for staff in staffList:
    print(staff)

