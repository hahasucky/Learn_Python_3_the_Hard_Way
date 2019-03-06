import datetime
my_date = datetime.date(2016,7,7)

class Employee :

    #class variable
    raise_amount = 0.1
    num_of_emps = 0

    #instance oper.
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

# How to inherit from a class
class developer(Employee):
    pass

class manager(Employee):
    def  __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)


    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print( "--->", emp.fullname())


# attribute and functions accessible
dev_1 = developer('Corey', 'Schafer', 50000) # Employee의 클래스 변수 사용
dev_2 = developer('Test', 'User', 60000)
# subclass => class instance 재정의 가능 / 피상속 클래스에 영향 없음
mgr_1 = manager("sue", "smith", 900000, [dev_1,dev_2])
mgr_1.print_emps()

mgr_1.remove_emp(dev_1)
mgr_1.print_emps()


## special method < isinstance >
print(isinstance(mgr_1, developer)) # is it a instance of a class? # False
print(issubclass(developer, Employee)) # inheritance test


# 클래스와 상속을 잘 사용하면, 쓸 데 없이 코드를 재사용할 필요가 없고
# 클래스별 커스터마이징 + 시스템적으로 변수 및 함수 공유를 통해 일목 요연하게, 변수의 값과 함수 적용을 관리할 수 있다.

#print(dev_1.pay)
#dev_1.apply_raise()
#print(dev_1.pay)

# real life example






#print(emp_1.pay)
#emp_1.apply_raise()
#print(emp_1.pay)

#Employee.raise_amount = 2 # class-shared variable of raise amount ( emp_2 share this )
#emp_1.raise_amount = 0.5 #instance variable of raise_amount # 변수 공간에 새로 들어가는 것. 클래스 배리어블 안씀
#print(emp_1.__dict__)
#print(emp_1.apply_raise())
#print(emp_2.__dict__)
#print(emp_2.apply_raise())
#print(Employee.num_of_emps)
#Employee.fix_class_raise_amount(0.5) # 클래스 변수 컨트롤 => 하향조정
#print(emp_2.apply_raise())

#emp_3 = Employee.str_to_emp("seokhee-han-6000000")
#print(emp_3.pay)
#print(Employee.num_of_emps)
#print(Employee.is_weekday(my_date))
