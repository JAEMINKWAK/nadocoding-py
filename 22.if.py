weather = "비"

if weather == "비": # =은 2번 써야 한다.
  print("우산을 챙기세요.")

weather = "맑음" # 맑음으로 바꾸면 실행 안됨.

if weather == "비":
  print("우산을 챙기세요.")

weather = "미세먼지"

if weather == "비":
  print("우산을 챙기세요.") # 1번
elif weather == "미세먼지":
  print("마스크를 챙기세요.") # 2번

weather = "맑아요"

if weather == "비":
  print("우산을 챙기세요.") # 1번
elif weather == "미세먼지":
  print("마스크를 챙기세요.") # 2번
else:
  print("준비물 필요 없어요.") # 3번

weather = input("오늘 날씨는 어때요? ")
# print(weather) # 사용자가 입력한 값 출력 # 주석 처리
if weather == "비":
  print("우산을 챙기세요.") # 1번
elif weather == "미세먼지":
  print("마스크를 챙기세요.") # 2번
else:
  print("준비물 필요 없어요.") # 3번

weather = input("오늘 날씨는 어때요? ")
# print(weather) # 사용자가 입력한 값 출력 # 주석 처리
if weather == "비" or weather == "눈": # 조건 변경
  print("우산을 챙기세요.") # 1번
elif weather == "미세먼지":
  print("마스크를 챙기세요.") # 2번
else:
  print("준비물 필요 없어요.") # 3번

temp = int(input("기온은 어때요? "))

if 30 <= temp: # 30도 이상이면
  print("너무 더워요. 나가지 마세요.")
elif 10 <= temp and temp < 30: # 10도 이상 30도 미만이면
  print("괜찮은 날씨에요.")
elif 0 <= temp and temp < 10: # 0도 이상 10도 미만이면
  print("외투를 챙기세요")
else: # 그 외의 모든 경우 (0도 미만이면)
  print("너무 추워요. 나가지마세요.")