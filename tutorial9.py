class Employee:
    increment = 1.5
    no_of_employees = 0

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
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

    @property
    def email(self):
        if self.fname is None:
            return 'Email not set'
        else:
            return self.fname + '.' + self.lname + '@email.com'

    @email.setter
    def email(self, given_email):
        name_list = given_email.split('@')[0].split('.')
        self.fname = name_list[0]
        self.lname = name_list[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


if __name__ == '__main__':
    durgesh = Employee('Durgesh', 'Parekh', 40000)
    rohan = Employee('Rohan', 'Roy', 9)
    print(durgesh.email, rohan.email)
    rohan.lname = 'Khurana'
    print(rohan.email)
    rohan.email = 'khurana.rohan@gmail.com'
    print(rohan.email)
    del rohan.email
    print(rohan.email)