name = "캔"
animal = "고양이"
age = 13
hobby = "잠"
is_adult = age >= 3

# 애완동물 소개

print("우리집 " + animal + "의 이름은 " + name + "이에요.") # 이름 소개
# 수정 전
# print(name + "는 " + str(age) + "살이며, " + hobby + "(을)를 아주 좋아해요")
# 수정 후
print(name, "는 ", age, "살이며, ", hobby, "(을)를 아주 좋아해요") # 나이, 취미 소개
print(name + "은 어른일까요?" + str(is_adult)) # 어른인지 여부 확인
