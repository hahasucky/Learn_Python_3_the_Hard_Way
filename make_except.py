class My_Error(Exception):
    def __str__(instance):
        return "욕설이나 음란어는 금지입니다. 금지입니다."

def say_nick(nick):
    if nick == '좆':
        raise My_Error()
    print(nick)

print("just func result")
say_nick('좆')


# 마이 에러라는 클래스가 익셉션으로 부터 클래스 베리어블과, 클래스 함수를 상속받았다.
