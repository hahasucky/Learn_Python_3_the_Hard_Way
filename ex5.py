# -*- coding: utf-8 -*-
from decimal import Decimal
user_name = 'seokhee. Han'
user_age = 25 # not a lie
user_height = 185.0 # cm
user_weight = 77.0 # kg
user_eyes = '블루색'
user_teeth = '화이트색' 
user_hair = '갈색'

print(user_height / 2.54)
print(user_weight / 0.4536)

print "%d살인 %s에 대해 이야기해 보죠" % ( user_age - 1, user_name )
print "키는 %0.1f인치고요." % (user_height / 2.54)
print "몸무게는 %^10.1f파운드이에요." % (user_weight / 0.4536)
print "사실 아주 많이 나가는 것은 아니죠." 
print "눈은 %s이고 머리는 %s이에요" % ( user_eyes, user_hair ) 
print "이는 보통 %s이고 커피를 먹으면 달라져요" % user_teeth 
# 이줄은 까다롭지만 잘 따라해보자 !!!
print "%d, %d, %d를 모두 더하면 %d랍니다." % (user_age - 1, user_height, user_weight, user_age - 1 + user_height + user_weight ) 
