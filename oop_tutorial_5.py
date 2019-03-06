import datetime
my_date = datetime.date(2016,7,7)

class Employee :

    #class variable
    raise_amount = 0.1
    num_of_emps = 0

    # @instance oper.
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps += 1 # __init__은 오브젝트 생성시마다 돌아감.

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) # or Employee.raise_amount
        return self.pay

    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.first, self.last, self.pay)
# 해당 오브젝트에 대한 정보를 더 편한 형태로 보고, 수정할 수 있게, 인스턴스화가능한 형태로 쓴다.

    def after_edit_original_member(self):
        Employee.num_of_emps -= 1

    def __str__(self): # simple string repre to show to other not knowing code
        return "{} - {}".format(self.fullname(), self.pay)

    def __add__(self, other):
        return self.pay + other.pay


    @classmethod
    def fix_class_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def str_to_emp(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_weekday(date):
        day_num = date.weekday()
        if date.weekday() == 5 or date.weekday() == 6:
            return False
        return ["mon","tue","wed","thu","fri"][day_num]


#emp_1 = Employee("han", "seokhee", 100000)
#print(emp_1)
#print(emp_1.__repr__())
#emp_1 = Employee('han','seokhee',200000)
#print(emp_1.__repr__())
#emp_1.after_edit_original_member()
#print(Employee.num_of_emps)
#print(emp_1.__str__())

# 해당 오브젝트에 대한 정보를 더 편한 형태로 보고, 수정할 수 있게, 인스턴스화가능한 형태로 쓴다.
#.__repre__ : argv repre for dev of a object
#.__str__ : string repre of object

emp_1 = Employee("han", "seokhee", 100000)
emp_2 = Employee("lee", "seokhee", 200000)

print(emp_2 + emp_1) # = emp_2.__add__(emp_1) + is defined in dunder add
# how i want + operand to be interpreted.
