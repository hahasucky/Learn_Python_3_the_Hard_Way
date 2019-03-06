# 달리기 대회 : 같은 이름의 아이들이 몇등을하고 있는지 맞추는 알고리즘을 짜라

# 유저 인풋 받기 : 찾고 싶은 사람 이름이 있나?
print("찾고 싶은 이름은 머에요?// 같은 이름 아이들의 퍼포먼스를 보세요.")
target_name = input(">")

# 레이스 엔드라인에서 입수된 순위정보
endline_checker = ['한석희','권황관','조원익','박용진','조원익','한석희','조원영','박우진','한석희']

# 파이썬 메소드들을 이용해 순위를 추적하는 루프 구성
이전_단계_발견된_인덱스 = endline_checker.index(target_name)
rank_list = []
rank_list.append(이전_단계_발견된_인덱스 + 1) # 첫 랭크 추가
for i in range(endline_checker.count(target_name) - 1):
    발견_인덱스 = endline_checker.index(target_name, 이전_단계_발견된_인덱스+1)
    이전_단계_발견된_인덱스 = 발견_인덱스
    rank_list.append((발견_인덱스+1))

# 프린트 해주기
for i in rank_list :
    print(f"{target_name}씨는 {str(i)} 위에서 발견돼씀.")
