숫자들 = [1,2,3,4,5]
과일들 = ['사과','귤','배','살구',]
잔돈들 = [1,'십원',3,5,'백원']

for 숫자 in 숫자들:
    print(f"이 수는 {숫자}")

for 과일 in 과일들:
    print(f"과일종류 : {과일}")

for i in 잔돈들:
    print(f"받은 잔돈 {i}")

원소들 = []

for i in range(6):
    print(f"list에 {i}를 더합니다.")
    원소들.append(i)

for i in 원소들:
    print(f"원소는 {i}")
