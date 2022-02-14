print("대기번호: 1")
print("대기번호: 2")
print("대기번호: 3")
print("대기번호: 4")

for waiting_no in range(5): # 0부터 5직전까지 (0 ~ 4)
  print(f"대기번호: {waiting_no}")

for waiting_no in range(1, 6): # 1부터 6직전까지 (1 ~ 5)
  print(f"대기번호: {waiting_no}")

starbucks = ["아이언맨", "토르", "아이엠 그루트"] # 손님 리스트
for customer in starbucks:
  print(f"{customer}, 커피가 준비되었습니다.")