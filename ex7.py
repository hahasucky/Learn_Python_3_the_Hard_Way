# -*- coding: utf-8 -*-

print("영희에겐 꼬마 양이 있지.")
print("양털은 {}처럼 새하얗네".format('눈')) # {}를 포맷문자로 사용하고, 포맷할 데이터를 .format(that data)에 넣음
print("그리고 영희가 가는 곳마다.")
print("." * 10) # 어떻게 될까요? 문자열에 * n 하면 10번이 concetenate 된다.

end1 = "맛"
end2 = "있"
end3 = "는"
end4 = "치"
end5 = "즈"
end6 = "버"
end7 = "거"

print(end1 + end2 + end3, end=' ') # print(str) /n print(str) 상황이면 => print(str, end='n개의/s')를
#넣으면 이어서 나오면서 내가 넣은 /s의 개수만큼 띄어진다.
print(end4 + end5 + end6 + end7)
