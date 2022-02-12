from random import * # random 모듈에서 모든 것들을 가져다 쓰겠다는 의미

print(random()) # 0.0 이상 1.0 미만의 임의의 값 생성

print(random() * 10) # 0.0 이상 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 이상 10 미만의 임의의 정수 값 생성
print(int(random() * 10) + 1) # 1이상 10 이하(11 미만)의 임의의 정수 값 생성

print(int(random() * 45) + 1) # 1 이상 46 미만의 임의의 정수 값 생성

print(randrange(1, 46)) # 1 이상 46 미만의 임의의 정수 값 생성
print(randint(1, 45)) # 1 이상 45 이하(45를 포함)의 임의의 정수 값 생성


# 로또 추첨번호를 위한 6개의 랜덤 수를 뽑기 위해 다음처럼 같은 문장을 6번 반복하면 서로 다른 6개가 나올 수도 있지만
# 중복 번호가 발생할 수도 있다.
# 각 문장은 서로 영향을 주지 않는 독립사건이기 때문이다.
# 이럴때는 random 모듈에서 제공하는 sample()이라는 함수를 이용하면 된다.

print(randint(1, 45)) # 1 이상 45 이하(45를 포함)의 임의의 정수 값 생성
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))