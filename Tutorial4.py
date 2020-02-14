
class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    raise_amount = 1.10
    
    def __init__(self, first, last, pay, pro_lang):
        super().__init__(first, last, pay)
        self.prg_lang = pro_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Corey', 'Shafer', 50000, 'Python')
dev_2 = Developer('Test', 'User', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

# isinstance checks to see if an instance is part of a class.
print(isinstance(mgr_1, Developer))  # this will be False
print(isinstance(mgr_1, Manager))  # this will be True

# isinstance checks to see if an class is a subclass of the second class.
print(issubclass(Developer, Employee))  # this will be True
print(issubclass(Manager, Developer))  # this will be False
