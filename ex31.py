# -*- coding: utf-8 -*-

print("""Which language do you wanna learn?""")
p_lang_num = input("1.python 2.c++")


if p_lang_num == "1" :
    print("""Nice Choice. It's the hottest language in 21Cself.
It could either be used for the following studys""")
    python_area_num = input("""1.Data Science 2.AI 3.AUTOMATION
Which area interests you?""")

    if python_area_num == "1":
        print("""You know the vision of em. register to our class C
Here is our class URL. COPYLINK : https://docs.python.org/3/tutorial/classes.html""")
    elif python_area_num == "2":
        print("""You know the vision of em. register to our class D
Here is our class URL. COPYLINK : https://docs.python.org/3/tutorial/classes.html""")
    elif python_area_num == "3":
        print("""You know the vision of em. register to our class E
Here is our class URL. COPYLINK : https:/docs.python.org/3/tutorial/classes.html""")
    else:
        print("""you might wanna just get to know python basics class. register to our class A
Here is our class URL. COPYLINK : https://docs.python.org/3/tutorial/classes.html""")


elif p_lang_num == "2" :
            print("""you might wanna just get to know C++ class. register to our alias teaching institution
Here is their class URL. COPYLINK : https://docs.python.org/3/tutorial/classes.html""")
            answer = input("""you might wanna just get to know C++ class. register to our alias teaching institution
Here is their class URL. COPYLINK : https://docs.python.org/3/tutorial/classes.html right?""")

else:
    print("You don't fit this codeacademy. Sir! Go look somewhere else.")
