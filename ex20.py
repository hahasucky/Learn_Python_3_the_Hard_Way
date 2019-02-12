# argv함수 가져오기
from sys import argv

스크립트, 입력_파일 = argv

# 사용할 세 개의 함수 정의
def 모두_출력(파일) :
    print(파일.read()) # file object를 받아서, 모든 스트링을 출력

def 되감기(파일) :
    파일.seek(0)

def 한_줄_출력(줄_수, 파일) :
    print(줄_수, 파일.readline())

# 입력 받은 파일의 파일 오브젝트 열기
현재_파일 = open(입력_파일, encoding = 'utf-8')

# 입력 받은 파일 전체를 출력해보기
print("파일 전체를 출력해봅시다.\n")
모두_출력(현재_파일)

# 되감아서, 커서를 제일 처음으로 돌리기
print("이번에는 테이프처럼 되감아봅시다.")
되감기(현재_파일)

# 세 줄을 출력해보자.
print("세 줄을 출력해봅시다.")

현재_줄_수 = 1
한_줄_출력(현재_줄_수, 현재_파일) # file_object.readline() 이후에, \n 이전까지 프린트 후, 커서는 다음줄 처음 문자.

현재_줄_수 += 1
한_줄_출력(현재_줄_수, 현재_파일)

현재_줄_수 += 1
한_줄_출력(현재_줄_수, 현재_파일)
