# -*- coding: utf-8 -*-

def 단어_쪼개기(값):
    '''문자열을 단어 단위로 쪼개줍니다.'''
    단어들 = 값.split(' ')
    return 단어들

def 단어_정렬(단어들): # input:lst     output:lst
    '''인풋 : 리스트 아웃풋 : 리스트(정렬된).'''
    return sorted(단어들)

def 첫_단어_출력(단어들): # input:list     output:str
    '''첫 단어를 꺼내고 출력합니다.'''
    단어 = 단어들.pop(0)
    return 단어

def 마지막_단어_출력(단어들): # input: list     output:str
    '''마지막 단어를 꺼내고 출력합니다.'''
    단어 = 단어들.pop(-1)
    return(단어)

def 문장_정렬(문장): # input: str     output: lst
    '''한 문장을 통째로 받아 정렬된 단어를 반환합니다.'''
    단어들 = 단어_쪼개기(문장) # uses other function to make a value to be assigned to a useful varia.
    return 단어_정렬(단어들) # uses other function to return wanted value to be later assigned to another variable

def 처음과_마지막_단어_출력(문장): # input:st     output:str, srt
    '''문장의 처음과 마지막 단어를 출력합니다.'''
    단어들 = 단어_쪼개기(문장)
    첫_단어_출력(단어들)
    마지막_단어_출력(단어들)

def 정렬_후_처음과_마지막_단어_출력(문장): # input:str     output:str, str, str
    '''단어를 정렬하고 처음과 마지막 단어를 출력합니다.'''
    단어들 = 문장_정렬(문장)
    첫_단어_출력(단어들)
    마지막_단어_출력(단어들)

# 다른 함수에 어떤 특정 기능, 함수오퍼레이션을 풀리 적지 말고, 다른 함수를 써놓고, 그 함수에서는 깔끔하게 !!
# 그 함수를 이용해서 값을 만들어 변수에 지정하고, 그 함수를 이용해 리턴값을 만들어내기도 해라 !!
