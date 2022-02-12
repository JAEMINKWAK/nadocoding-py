python = "Python is Amazing"

print(python.lower()) # python is amazing
print(python.upper()) # PYTHON IS AMAZING
print(python[0].isupper()) # True: 0번째 인덱스의 값이 대문자인지 확인
print(len(python)) # 17: 띄어쓰기를 포함한 문자열의 전체 길이 (length)
print(python.replace("Python", "Java")) # Java is Amazing

index = python.index("n") # 처음으로 발견된 n의 인덱스
print(index) # 5: Python의 n
index = python.index("n", index + 1) # 6번째 인덱스 이후에 처음으로 발견된 n의 인덱스
print(index) # 15: Amazing의 n

find = python.find("n") # 처음으로 발견된 n의 인덱스
print(find) # 5: Python의 n
find = python.find("n", find + 1) # 6번째 인덱스 이후에 처음으로 발견된 n의 인덱스
print(find)

# index() 사용 시 에러가 발생하면 이후의 문장은 실행되지 않고
# 프로그램이 종료되어 버리므로, find() 를 사용하는 문장을 실행하기 위해서는
# 앞 문장을 없애거나 주석 처리 해주세요.

print(python.index("Java")) # Java가 없기 때문에 에러가 발생하며 프로그램 종료
print(python.find("Java")) # Java가 없으면 -1을 반환(출력)하며 프로그램 계속 수행

print(python.count("n")) # 2: 문자여 내에서 n이 나온 횟수