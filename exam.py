# -*- coding: utf-8 -*-
import sys
스크립트명, codec, err_method = sys.argv

def main(file_object, codec, err_method):
    a_target_line = file_object.readline()

    if a_target_line :
        one_line_print(a_target_line.strip(), codec, err_method)

        return main(file_object, codec, err_method) # 또 그 함수를 실행


def one_line_print (a_line, codec, err_method):
    encoded_line = a_line.encode(codec, errors = err_method)
    decoded_line = encoded_line.decode(codec, errors = err_method)
    print(decoded_line, "<==>", encoded_line)

# languages.txt를 읽어오고, 스크립트 옆에 실행변수로 받은 유저의 인코딩 출력 설정을 반영해서 함수에 넣으줌
f_o_languages = open('languages.txt', encoding = 'utf-16')

main(f_o_languages, codec, err_method)
