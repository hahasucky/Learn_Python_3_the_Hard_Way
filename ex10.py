# -*- coding: utf-8 -*-

탭_냥이 = "\t난 탭이 됨."
줄_냥이 = "나는\n분리됨."
역슬래시_냥이 = "나는 \ 고 \ 양이."

뚱뚱_냥이 = """
할 일 목록:
\t* 고양이 밥
\t* 물고기
\t* 개박하\n\t* 오리새
"""

print(탭_냥이)
print(줄_냥이)
print(역슬래시_냥이)
print(뚱뚱_냥이)

print('barca \ a')

print('''
where am i
am i heading to
right direction.
''')

height = 172.872
weight = 76.877
name = "Seokhee Han"

print('my name is %s.\nmy height\\\t%0.1f\vand\vmy weight\\\t%0.1f\n\'waiting for somebody\'\b\b\b\bhody' % ( name, height, weight ))

print("a\b", end="")
print("a\b", end="")
print("a\b", end="")
print("h\b", end="")
