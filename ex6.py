# -*- coding: utf-8 -*-      # < 한글 인코딩 : ㅋㅋ 이 줄도 # 해시로 주석을 달 수 있음. !! >

x = "세상에는 %d 종류의 사람이 있어요." % 10  # 십진수 포매팅
binary = "이진수" # 변수에 스트링 지정
do_not = "모르는"
y = "%s를 아는 사람과 %s 사람" % (binary, do_not) # 스트링 포매팅 # 한글 스트링은 %s로만 받아라
z =  'How fun is it!'

print x
print y
print z

print "'%s'라고 했어요." % x # 한글 스트링 변수를 포맷문자 %r로 받을 때 인코딩 오류가 생기는 이유가 멀까? 영어는 안생긴다. / 한글 스트링을 포맷팅 할 때는 => %s 를 하여, 컴퓨터가 인식한 한글을 출력용 인간 한글로 바꿔줄 필터를 적용해야한다. 
print "'%s'이라고도 했죠." % y
print "So, %r" % z # 불린 자료형은 포매팅하려면, %r

hilarious = True
joke_evaluation = "웃기는 농담 아니에요?! %r" # "%s 스트링" %스트링 이렇게 바로 뒤에 포맷 문자에 넣을 변수가 없어도 됨.

print joke_evaluation % hilarious # 나중에 이렇게 변수로 대표하고 뒤에 이어도 유효함.

l = "이 문자열의 왼쪽->"
r = "<-이 문자열의 오른쪽 "
print l + r 