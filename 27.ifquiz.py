from random import * # random 모듈에서 모든 것들을 가져다 쓰겠다는 의미

for i in range(1, 51):
  time = int((random() * 45) + 5) # 5 ~ 50
  if time >= 5 and time <= 15:
    print(f"[O] {i}번째 손님 (소요시간:{time}분)")
  else:
    print(f"[ ] {i}번째 손님 (소요시간: {time}분)")