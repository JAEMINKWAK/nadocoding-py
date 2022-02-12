# 지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway) # [10, 20, 30]

subway = ["유재석", "조세호", "박명수"]
print(subway) # ['유재석', '조세호', '박명수']

# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호")) # 1 (인덱스는 0부터 시작한다는 것, 기억하자.)

# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway) # ['유재석', '조세호', '박명수', '하하']

# 정형돈씨를 유재석 / 조세호 사이에 태움
subway.insert(1, "정형돈") # 인덱스 1 위치에 삽입
print(subway) # ['유재석', '정형돈', '조세호', '박명수', '하하']

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop()) # 하하 내림
print(subway) # ['유재석', '정형돈', '조세호', '박명수']

print(subway.pop()) # 박명수 내림
print(subway) # ['유재석', '정형돈', '조세호']

print(subway.pop()) # 조세호 내림
print(subway) # ['유재석', '정형돈']

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석") # 설명을 위해 유재석씨를 맨 뒤에 태운다.
print(subway) # ['유재석', '정형돈', '유재석']
print(subway.count("유재석")) # 유재석씨가 2명

num_list = [5, 2, 4, 3, 1]

num_list.sort() # 정렬
print(num_list) # [1, 2, 3, 4, 5]

num_list.reverse() # 순서 뒤집기
print(num_list) # [5, 4, 3, 2, 1]

# 모두 지우기
num_list.clear()
print(num_list) # []

mix_list = ["조세호", 20, True] # 다양한 자료형을 함께 사용할 수 있다.
print(mix_list) # ['조세호', 20, True]

num_list = [5, 2, 4, 3, 1] # num_list 값 다시 정의
num_list.extend(mix_list) # 리스트 확장
print(num_list) # [5, 2, 4, 3, 1, '조세호', 20, True]