# -*- coding: utf-8 -*-

def 비밀_공식(시작):
    젤리알 = 시작 * 500
    그릇 = 젤리알 / 1000
    상자 = 그릇/ 100
    return 젤리알, 그릇, 상자

시작점 = 10000

공식 = 비밀_공식(시작점)

#리스트 = [1000, 100, 10]
#튜플 = (1000, 100, 10)
스트링 = 'abc'
print("젤리 {}알 {}그릇 {}상자가 있습니다.".format(*스트링))
print(스트링)
