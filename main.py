class Employee:
    increment = 1.5
    no_of_employees = 0

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        # self.increment = 1.4
        Employee.no_of_employees += 1

    def increase(self):
        self.salary = int(self.salary * self.increment)

    @classmethod
    def change_increment(cls, amount):
        cls.increment = amount

    @classmethod
    def from_str(cls, emp_string):
        fname, lname, salary = emp_string.split('-')
        return cls(fname, lname, salary)

    @staticmethod
    def isOpen(day):
        if day =='sunday':
            return False
        else:
            return True


class Programmer(Employee):
    def __init__(self, fname, lname, salary, proglang, exp):
        super().__init__(fname, lname, salary)
        self.proglang = proglang
        self.exp = exp

    def increase(self):
        self.salary = int(self.salary * (self.increment + 0.2))


# kirti = Programmer('Kirti', 'Borse', 60000)
durgesh = Programmer('Durgesh', 'Parekh', 40000, 'Python', '1 Year')
# print(durgesh.__dict__)
help(Programmer)
# rohan = Employee('Rohan', 'Roy', 54000)

# henil = Employee.from_str("henil-patel-123456")

# print(henil.__dict__)

# Employee.change_increment(3)
# harry.increase()
# print(harry.salary)
# harry.increase()

# print(harry.__dict__, harry.salary)
# harry.increment = 9
# print(harry.__dict__)
