from random import * # random 모듈에서 모든 것들을 가져다 쓰겠다는 의미

cnt = 0 # 총 탑승 승객 수
for i in range(1, 51):
  time = int((random() * 45) + 5) # 5 ~ 50
  # time = randrange(5, 51) 5 ~ 50 분 사이
  if time >= 5 and time <= 15:
    print(f"[O] {i}번째 손님 (소요시간:{time}분)")
    cnt += 1 # 총 탑습 승객 수 증가 처리
  else: # 매칭 실패한 경우
    print(f"[ ] {i}번째 손님 (소요시간: {time}분)")

print(f"총 탑승 승객: {cnt}분")