# -*- coding: utf-8 -*-
# exit을 쓰기 위해 모듈로 부터 불러
from sys import exit

# 출발 함수 정의
def 출발():
    print("어두운 방에 있습니다.")
    print("오른쪽, 왼쪽 양쪽으로 문이 있군요")
    print("어디를 고를래요?")

    선택 = input("> 왼쪽 이랑 오른쪽만 넣어 아니면 죽어!! ")

    if 선택 == "왼쪽":
        곰_방() # 곰_방() 함수 반환
    elif 선택 == "오른쪽":
        크룰루_방() # 크룰루_방() 함수 반환
    else:
        exit("정상적인 접근이 아닙니다!")

#죽음 함수 정의
def 죽음(메세지):
    print(메세지, "노오오오력 만큼은 .... ㅇㅈ요 GAAAAMEOOOOVER")
    exit(1) #문제없이 프로그램 종료

# 크룰루_방() 함수 정의
def 크룰루_방():
    print("대악마 크룰루네 !!!")
    print("그분이 당신을 뚤어지게 노려봅니다. 너는 식겁했네요")
    print("목숨을 위해 달아날거냐? 아니면 니 머리를 먹으려냐?")

    선택 = input("> 어떠 어떠하게 달아나기랑 어떠어떠하게 먹기만 선택해!!")

    if "달아나기" in 선택: # string membership bool expression => 그 스트링 도중에 해당되기만 하면
        출발()
    elif "먹기" in 선택:
        죽음("헤헤헤ㅔ헤헤 맛있도다아ㅏ아아ㅏ!!!...")
    else:
        크룰루_방()

#곰_방() 함수 정의
def 곰_방():
    print("여기에는 곰이 한마리 있어용")
    print("곰은 꿀을 잔뜩 들고 있군요")
    print("곰이 다른 쪽 문앞에 뻐튕기고 있군요")
    print("어떻게 곰을 움직이겠습니까? 꿀 뺏기 랑 곰 놀리기 만 선택해")
    곰의_움직임 = False #처음에 False로 해놓고, 루프 처음에 True로 변환하고, 다음 순환때 True조건을 씀

    while True:
        선택 = input("> ")

        if 선택 == "꿀 뺏기":
            죽음("곰이 당신을 쳐다보더니 엄청난 세기로 가격!!")

        elif 선택 == "곰 놀리기" and not 곰의_움직임:
            print("you are now free.")
            print("그 담엔 \"문 열기\" 또는 또 \"곰 놀리기\"?")
            곰의_움직임 = True # 곰을 한번 놀리면, 곰이 문을 열어주는데, 그담에 또 놀리면 ㅈ 되게 하려고
            # 곰의_움직임 상태 변환 => elif로 가면 같은 선택 해도 ㅈ됨

        elif 선택 == "곰 놀리기" and 곰의_움직임:
            죽음("극대노!! 곰 킬유 유 다이!! 바이바이")

        elif 선택 == "문 열기" and 곰의_움직임:
            황금_방()
        else:
            print("무슨 말이셔? 곰 놀리기랑 꿀 뺏기 중에 하나만 골라 컴터자나!!")

#황금방() 함수 정의
def 황금_방():
    print("a room full of goldbars!!! how much gonna take?")

    선택 = input("> 꼭 0과 1을 포함하는 액수를 써 제발 ")
    if "0" in 선택 or "1" in 선택: # 스트링 멤버쉽 테스트
        액수 = int(선택)
    else:
        죽음("왜케 꼬질 꼬질하게 숫자쓰냐 ... 이런 거부터 배워라 !! 배워라!! 오바!!")

    if 액수 < 50:
        print("좋아 욕심 부리지 않는 군요!! 당신이 우승자!!")
        exit(0)
    else:
        죽음("욕심쟁이 색기야!! 그냥 나가!!")

# 출발함 수 부터 실행
출발()

# 함수는 일일이 포함시키고 싶지 않을 때, 간단하게 하기 위해 사용할 수 있습니다. / 같은 기능을 반복해야할 때 : 함수를 만들고 씁니다.
