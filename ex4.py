# -*- coding: utf-8 -*-

cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "자동차", cars, "대가 있습니다."
print "자동차 %s대가 있습니다." %cars
print "운전자는", drivers, "명 뿐입니다."
print "오늘은 빈 차가", cars_not_driven, "대 일 것입니다."
print "오늘은",carpool_capacity, "명을 태울 수 있습니다."
print "함께 탈 사람은",passengers, "명 있습니다."
print "차마다,", average_passengers_per_car, "명 정도씩 타야합니다."

# 4.2 더해보기
# 1. 왜 space_in_a_car 을 부동 소수점으로 썼을까? 
# 여기가 버스와 기사를 관리해서, 학교 또는 관광회사에 기사와 버스를 제공하는 회사라고 해보자. 
# 변수에 따른 값, 차 대수, 금일 기사수, 단위 차량 당 가능 수용인원 수, 해당 이벤트에 다뤄야하는 승객 수 는 끊임없이 변할 것이다.
# 사칙연산을 할때, 곱 + 나눗셈을 할때, 소수점 자리까지 정확하게 연산이 가능하다. 임의로 '내림' 이 되거나 하지 않는다.
# 대당 수용 인원을 float로 설정한다면, 정확한 평균 지수들을 측정할 때 좋을 것이다.
# 한달에 이벤트들을 커버하고, 통계를 내어,      total_event * average_empty_seat/ (total_event * space_in_a_car) 으로 나눠 평균 몇 퍼센트의 좌석이 낭비되는 지 추산할 수 있다.
# 2. 머가 달라질까 ?
# 소수점 단위의 사칙연산을 통해 => 어떤 지수나 필요한 수치를 더 정확하게 계산해낼 수 있다.
# 부동소수점을 포함하여 사칙연산을 하면 => !! 결과도 무조건 부동소수점 까지 표현되어 나온다. 
# 3. 모든 변수에 대해 주석을 달아라 해시 문자를 통해.
# 딱히 달아야할 내용이 없다. 그냥 변수 명에 대한 한글 해석 정도 밖에 생각이 안난다.
# 4. = 는 오른 쪽에 오는 < 값 > 에 '이름', '의미'를 붙일 때 사용한다.
# 5. _는  underscore 또는 밑줄 문자라고 부른다.
