# -*- coding: utf-8 -*-

사람 = 20
차 = 20
트럭 = 40

if not(사람 >= 차 or 사람 >= 트럭): # 만약 if 다음의 불표현식이 True면 내 :이후 블록을 실행해
    print("개꿀띠.")
elif not(사람 < 차 and 사람 < 트럭): # 만약  if 문이 True여서 실행되지 않으면, 나의 조건이 True 이면 실행해
    print("평타구마.")
else: # 만약 if 문이 true 가 아니라면 ( 나아가 elif 가 있을 때, 불표현이 True가 아니였다면, 나 else: 의 블록을 실행해라)
    print("힘들겠다.")

# else 꼭 필요하진 않음. 그냥 elif 조건까지 안맞으면 넘어가면 된다.
