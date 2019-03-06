class Student :
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    @fullname.setter # setter should use the same name of the function.setter
    def fullname(self, input):
        first, last = input.split(' ')
        self.first = first
        self.last = last # 변수 재설정 후 그 함수로

    @fullname.deleter # setter should use the same name of the function.setter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None
    # del emp_1.fullname
    @property
    def email_ad(self):
        return "{}_{}@cv_10.com".format(self.first, self.last)
    @email_ad.setter # 누군가가 프로퍼티화 된 메소드에 어싸인먼트를 했을때, 그 값으로부터 => 메소드에 넣을 정의역을 뽑아오는 역할
    def email_ad(self, sep_assign_email):
        self.first, self.last, unused = sep_assign_email.replace("@",' ').replace("_"," ").split(' ')


stu_1 = Student("seokhee", "han")
stu_1.email_ad = "sucky_han@naver.com" # can't assign sth to a call of a function
# instance화 된 메소드에게 원래 역할대로 메소드 역할을 하게 하려면, = "목표를 위한 정의역" => 세터가 이것을 가져가서 변수에 지정 =>
# => 원래함수가서 리턴할 값 작
print(stu_1.email_ad)
del stu_1.fullname
print(stu_1.fullname)
