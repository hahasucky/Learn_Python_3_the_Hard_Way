# -*- coding: utf-8 -*-
#<1> 나이, 키, 몸무게 정보 유저 인풋
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()
## 문장으로 프린트
print(f"So, you're {age} old, {height} tall and {weight} heavy.")

#<2> 파일의 이름을 스크립트 사용자에게 인풋 받음 => 그거를 뽑아주는 부분
from sys import argv
script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

#<3> 이스케이프 문자열과 출력 룰
print('Let\'s practice everything.')
print('''You\'d need to know \'bout escapes
with \\ that do \n newlines and \t tabs.''')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
des_boundary = '--------------'

print(des_boundary, '\n', poem, '\n', des_boundary)

#<4> Variable designation, unpacking the result of function as a tuple
five = 10 - 2 - 3
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars * 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

# <5> 포매팅, 튜플인 함수 결과 *로 각 포매팅 자리에 배정.
# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))


# <6 logic : if => grammar / coop : boolyn true or false / shorthand operation >
people = 20
cats = 30
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")

dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")


if people == dogs:
    print("People are dogs.")
