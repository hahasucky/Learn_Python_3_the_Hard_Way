class student:

    def __init__(self, first, last, id):
        self.first = first
        self.last = last
        self.id = id

    @property
    def email(self):
        if self.last == None :
            print("the object's email has been deleted. assign another email")
            raise NameError
        else:
            return f"{self.last}_{self.id}@cv10.com"
    #@email.setter
    #def email(self, edited_):
    @email.setter
    def email(self, edited_email):
        self.last, self.id, unused_var = edited_email.replace('_', ' ').replace('@', ' ').split(' ')
    @email.deleter
    def email(self):
        self.last = None
        self.id = None


stu_1 = student("seokhee", 'han', '7616tjrgml')
print(stu_1.email)
# oh! stu_1's last name is 'kim' and he likes 'tjrgml9830' as his id
stu_1.last = "kim"
stu_1.id = "tjrgml9830"
print(stu_1.email)
# hmm someone might think .email as a instance and put an updated email address
# in that case I would like to update the whole object's instance variable
# and finally make it possible to enable him to get just as he wrote after =
# when he refer to email by that

# use setter so that i could extract some defining feature from the input =>
# redefine instance vars
# put it all back into the method so that it could pop out just as the input_person wants

stu_1.email = "jung_tjrgml7616@cv10.com" # i would extract defining instance variable change => redefine instance
# variable => put it back into the original function so that it could pop out just as you wanted it to be.
print(stu_1.email)


# hmm i would like to reset the objects reset variable and reference statusselfself.
# i don't want it to show that emailself.

del stu_1.email #이걸 통해 => 딜리터 함수에 접근해서 => 인스턴스 변수를 지우는 결과를 내야함, 참고하면 NameError 또는 None 리턴
print(stu_1.email)
