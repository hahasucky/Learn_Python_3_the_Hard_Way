class Korea_students:
    def __init__ (instance, name, city, age):
        instance.name = name
        instance.city = city
        instance.age = age

    def printall(instance):
        print(instance.name, instance.city , str(instance.age))


student_1 = Korea_students("한석희", "전주", 26)
# = 왼쪽의 인스턴스가 => instance에 지정되고
# => 인풋이 패스되어 => 인스턴스 변수들에 지정이 된다.

student_1.printall()
# 왼쪽의 인스턴스가 메소드의 instance로 들어가고, 함수가 계산된다.
# 내가 안넣어도 자동

Korea_students.printall(student_1)


# 어떤 관심 그룹이 있고
# 그 그룹의 각각 예시들의 정보를 필요한거 딱딱 정리해서 받고
# 그 정보들을 가공하여 유의미한 수치나, 목표 데이터를 만들어내어 이용하고 싶을 때.
