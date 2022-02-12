print(1 + 1) # 2
print(3 - 2) # 1
print(5 * 2) # 10
print(6 / 3) # 2

print(2 ** 3) # 2의 3제곱 = 2^3 = 8
print(5 % 3) # 5를 3으로 나눈 나머지 = 2
print(10 % 3) # 10을 3으로 나눈 나머지 = 1
print(5 // 3) # 5를 3으로 나눈 몫 = 1
print(10 // 3) # 10을 3으로 나눈 몫 = 3

print(10 > 3) # True
print(4 >= 7) # False
print(10 < 3) # False
print(5 <= 5) # True

# 좌항과 우항이 같은지 비교
print(3 == 3) # True
print(4 == 2) # False
print(3 + 4 == 7) # True

# 좌항과 우항이 다른지 비교
print(1 != 3) # True

# 좌항과 우항이 모두 참인가?
print((3 > 0) and (3 > 5)) # 좌항(3 > 0)은 참이지마나 우항(3 > 5)은 거짓이므로 False

# 좌항 또는 우항 중 하나라도 참인가?
print((3 > 0) or (3 > 5)) # 좌항(3 > 0)이 참이므로 우항(3 > 5)이 거짓이라도 True

# 좌항과 우항이 다른지 비교한 결과의 반대
print(not(1 != 3)) # 1과 3은 다르므로 True인데, True의 반대이므로 False

# 연속적인 수식에 대해서도 연산이 가능
print(5 > 4 > 3) # (5 > 4)도 참이며 (4 > 3)도 참이므로 True
print(5 > 4 > 7) # (5 > 4)는 참이지만 (4 > 7)은 거짓이므로 False