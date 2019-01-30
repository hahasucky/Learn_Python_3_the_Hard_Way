# -*- coding: utf-8 -*- #한글 출력하려면 이 인코딩 메져를 빼놓지 말자.
formatter = "{} {} {} {}" #formatter라는 변수에 {} {} {} {} 라는 문자열을 assign하였다. 뒤에 .format 함수가
#인자들과 함께 온다면, {}는 더이상 literal한 {}라는 문자로 출력되지 않고, 포맷문자열로 사용되게 된다.

print(formatter.format(1,2,3,4)) #스트링이 format이라는 함수를 호출했다, 그리고 내가 넣은 실행인자 4개를 함수에 넘겨 주었다.
print(formatter.format("하나","둘","셋","넷")) # 그러자 함수는 포매터 변수의 포매팅문자열 {}에 받은 인자를 넘겨서 대응시켜주었다.
print(formatter.format(True, False, False, True)) # 프린트 안의 결과는 대응된 이후의 '문자열'이다.
print(formatter.format(formatter,formatter,formatter,formatter)) # 포매터 변수 내의 {}도 .format함수를 만나지 않으면 그저
#문자그대로 {}로 출력된다. 다만, 그 함수를 만나면 그 의미가 사라질 뿐이다.

print(formatter.format(
"난 이게 있죠.",
"지금 막 써 주신 그것.",
"하지만 '노래'하진 않아요.",
"그러니까 잘자요.",
))

# print()할때, 꼭 한줄안에 우겨넣어서 인풋할 필요가 없을 것이다.
# "어차피 한줄에 출력될 것이긴 하지만 ", 쓸 때 불편하면, 위와 같이 '(' 를 ')'로 잘 닫아주기만 한다면, 여러줄로 늘여서 써도 된다.
# print()함수의 end = ''에 대해서 더 알아보자 ... 궁금하다, 출력 줄 바꾸기를 어떻게 통제할지. 
#
#
#
#
#
#
#
