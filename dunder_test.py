class Employee:

    def __init__(self, first, last, email, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return "{}_{}@company.com".format(self.first, self.last)
    @email.setter
    def email(self, new_email_ad):
        first, last, useless = new_email_ad.replace('_', ' ').replace('@', ' ').split(' ')
        self.first = first
        self.last = last

    def fullname(self):
        return "{} {}".format(self.first, self.last)


    def __repr__(self): # another dev, database managers // how would you print the object if you put it in print() func
        return "Employee('{}','{}','{}',{})".format(self.first, self.last, self.email, self.pay)

    def __add__(self, other):
        return ( self.pay + other.pay )

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee("seokhee", "han", "7616tjrgml", 5000000)
emp_2 = Employee('seokhee','kim','tjrgml12',8000000)

# 다른 개발자가, email을 인스턴스 변수로 알고 있을때, @property를 이용해 : 인스턴스.변수로 리턴 값에 접근가능
# 다른 개발자가, 변수 업뎉을 하려할때 => 그게 그 인스턴스의 .first , .last 로 지정 => 함수로 가서 값을 리턴
