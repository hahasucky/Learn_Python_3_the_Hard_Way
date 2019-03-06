class A:
    def rk(self):
        print(" In class A")
class B(A):
    def rk(self):
        print(" In class B")
class C(A):
    def rk(self):
        print("In class C")
class D(A):
    def rk(self):
        print("In class D")

# classes ordering
class E(D,C,B):
    pass

print(E.__mro__)
r = E()
r.rk()

# depth first search

#A -> B     -> E 상속시 인자순 ??
#     C
#     D
# D first for mro => 상속 실행인자중 더 먼저인 것  C =>  그 다음 B => A
