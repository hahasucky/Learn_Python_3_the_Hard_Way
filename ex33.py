# -*- coding: utf-8 -*-


def index_nums(num, 공차):

    숫자들 = []

    for i in range(0, num, 공차):
        print(f'꼭대기에서 i는 {i}')
        숫자들.append(i)
        print('숫자는 이제: ', 숫자들)
        print(f'바닥에 i는 {i}')

    print("숫자: ")
    for 숫자 in 숫자들:
        print(숫자)

index_nums(8, 2)
