import datetime

def time_decorator(func):
    def decorated_output():
        print(datetime.datetime.now())
        func()
    return decorated_output


@time_decorator
def first_appearance():
    print("적이 첫 출현했다!!")

first_appearance()


#first_appearance

#정의된 함수에 대해서

#함수명은 이제  function object이다.
#함수명([인자])를 하면, 함수 object안의 내용이 실행되고 종료하면서 return 이후의 값을 반환한다.
