from random import * # random 모듈에서 모든 것들을 가져다 쓰겠다는 의미

lst = range(1, 21) # 1부터 21 직전까지의 연속된 숫자 모음

lst = list(lst) # range를 list로 변환
shuffle(lst) # 리스트를 뒤섞기

winners = sample(lst, 4) # lst 리스트에서 중복 없이 4명 추첨

print("---당첨자 발표---")
print("치킨 당첨자: {0}".format(winners[0])) # 0번째 인덱스(1명)
print("커피 당첨자: {0}".format(winners[1:])) # 1번째부터 마지막까지 슬라이싱 (3명)
print("축하합니다!")