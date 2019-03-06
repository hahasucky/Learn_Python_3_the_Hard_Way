class Employee:
# class variable : variable shared among all instances that belongs to the class.
# what kind of variable to share among all employee
    # genrally applied variable within the class

    def __init__(self, last, pay, raise_amount): # instance variable : unique to that instance
        self.last = last
        self.pay = pay

    def name_money(self):
        return '{}{}'.format(self.last, self.pay)

    def apply_raise(self):
        self.pay = int( self.pay * self.raise_amount ) # self.raise_amount

    raise_amount = 1.04

# instance have it? => class origin have it?
# class as a category and shared traitself
# instance as have a unique, specified value and thus different output from the
# methodsself.

seokhee = Employee( "han", 100000, 1.1 )
print(Employee.__dict__) # show name space of the object seokhee
print(seokhee.__dict__)
