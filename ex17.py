# -*- coding: utf-8 -*-

from sys import argv
from os.path import exists

스크립트, 원본_파일, 복사_파일 = argv

print(f"{원본_파일}에서 {복사_파일}로 복사합니다.")

입력_파일 = open( 원본_파일, encoding = 'utf-8')
복사할_스트링 = 입력_파일.read()
# 복사할_스트링 = open( 원본_파일, encoding = 'utf-8').read()

print(f"{원본_파일}은 {len(복사할_스트링)}바이트입니다.")

print(f"출력할 파일이 존재하나요? {exists(복사_파일)}")
print("준비되었습니다. 계속하려면 엔터키를, 취소하려면 컨트롤 + 씨 키를 눌러주세요.")
input("어떻게 하시겠습니까?")

출력_파일_오브젝트 = open(복사_파일, 'w', encoding = 'utf-8')
출력_파일_오브젝트.write(복사할_스트링)

print("완료되었습니다")

입력_파일.close()
출력_파일_오브젝트.close()
