# -*- coding: utf-8 -*-

Que_1 = "몇 살이죠?"
Que_2 = "키는 몇이죠?"
Que_3 = "몸무게는 얼마죠?"

print(Que_1, end= " ")
나이 = input()
print('\033[{}C\033[1A'.format(len(Que_1) + len(나이) + 1))
print(Que_2, end= " ")
키 = input()
print('\033[{}C\033[1A'.format(len(Que_2) + len(키) + 1))
print(Que_3, end= " ")
몸무게 = input()
print('\033[{}C\033[1A'.format(len(Que_3) + len(몸무게)+ 1))
