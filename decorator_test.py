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
