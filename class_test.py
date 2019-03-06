class Employee:

    # < class variable assig >
    class_Emp_size = 0


    # < instantiate and init info >
    def __init__(self, last, email, pay):
        self.last = last
        self.email = email
        self.pay = pay


        print("one object of Employee class just instantiated.")
        Employee.class_Emp_size += 1 # 접근 방법 class_name / . [dot operator] / key !
        self.how_first = Employee.class_Emp_size


    # < methods >
    # < instance method >
    #method 1
    def fullname(self):
        return f"kodaesang {self.last}"
    #method 2
    def email_ad(self):
        print(f"this is {self.how_first}(st or th) email address")
        return f"{self.email}@korea.ac.kr"
    #method 3
    def salary_raise(self):
        return self.pay * self.raise_amount # self.raise_amount 를 참고해서 찾아와야함
    #method 4
    def __repr__(self): #dunder repr => 특정 오브젝트가 인스턴스화 될때, 어떤 실행인자가 들어갔는지 보여주는 것.
        return "Employee('{}', '{}', {})".format(self.last, self.email, self.pay )
    #method 5
    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email_ad())

    # < class method >
    @classmethod #method that passes class entity as a first arg. variable
    def str_to_a_emp(cls, str):
        last, email, pay = str.split(' ')
        return cls(last, email, pay)

    # < class's static method >
    @staticmethod
    def printer(str):
        print(str)



###########------class as a blueprint for samll module ended ------- #########

    # < instantiation : it includes construct thru class method >
stu_1 = Employee("han", "7616tjrgml", 120000)
stu_2 = Employee("kim", "tjrgml12", 110000)
stu_3 = Employee.str_to_a_emp("mok mokmok12 100000")

###########------ Inheritance momclass : Employee / subclass : devs, manags. ------- ###########
class developer(Employee):
    def __init__ (self, last, email, pay, prog_lang = None ):
        super().__init__(last, email, pay) # self안넘김필요한 부분에 대해서만 실행인자 넘김, mom class의 __init__ 메소드 사용해서 변수 지정
        if prog_lang is None:
            self.prog_lang = []
        else:
            self.prog_lang = [i for i in prog_lang if i != "Python"]

dev_1 = developer("kim", "kimmy07", 100000, ["Java", "Python"])
print(developer.__mro__)
print(dev_1.__dict__)


print(stu_1.__repr__())
print(stu_3.__str__())

#now! : __init__ , __repr__, __str__ 이 세개는 정말 자주 사용하실거에요. 클래스 쓸때!!


#왜 super().__init__(self,)안넘기나 ?
#다른 클래스의 메소드, 변수구조를 차용하고, 일부만 커스터마이징 하고 싶을 때 쓰자.
