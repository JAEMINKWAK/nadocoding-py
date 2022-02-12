print("a" + "b") # ab
print("a", "b") # a b

# 방법 1
print("나는 %d살입니다." % 20) # 나는 20살입니다.
print("나는 %s을 좋아합니다." % "파이썬") # 나는 파이썬을 좋아합니다.
print("Apple은 %c로 시작한다." % "A") # Apple은 A로 시작한다.

print("나는 %s살입니다." % 20) # 나는 20살입니다. (%s 로도 정수값 표현 가능)


print("나는 %s색과 %s색을 좋아한다." % ("파란", "빨간")) # 나는 파란색과 빨간색을 좋아한다.

# 방법 2
print("나는 {}살이다.".format(20)) # 나는 20살이다.
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간")) # 나는 파란색과 빨간색을 좋아해요.
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간")) # 나는 파란색과 빨간색을 좋아해요.
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간")) # 나는 빨간색과 파란색을 좋아해요.

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))
# 나는 20살이며, 빨간색을 좋아해요.
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age=20))
# 나는 20살이며, 빨간색을 좋아해요.(.format 뒤에 순서를 변경해도 괜찮다.)

# 방법 4
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")
# 나는 20살이며, 빨간색을 좋아해요.