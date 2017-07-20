"""
 UP/DOWN
"""
# 랜덤 모듈 추가
import random

n = random.randint(1, 20)   # 1에서 20까지 랜덤수 생성

# 무한루프
while True:
    # 입력시작
    user = input("1~20까지 숫자를 입력하세요.")
    user = int(user)

    # 맞춘 경우 종료
    if n == user:
        print("성공!! : " + str(n))
        break

    if user < 1 or user > 20:
        print("입력오류")
        continue

    # UP/DOWN 표시
    if n > user:
        print("숫자 UP!!")
    else:
        print("숫자 DOWN!!")

