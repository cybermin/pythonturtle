"""
python 예제 : 반복해서 선 그리기
"""

import turtle as t

# 입력
n = input("숫자를 입력하세요.")
n = int(n)

angle = input("각도를 입력하세요.")
angle = int(angle)


t.bgcolor("black")  # 화면 배경색 변경
t.speed(0)           # 속도 지정 : 가장 빠르게

# 선 그리기
for i in range(n):
    if i % 3 == 0 : t.color("red")   # 펜 색 지정
    elif i % 3 == 1 : t.color("blue")
    else : t.color("yellow")

    t.forward(i*2)
    t.left(angle)

# 화면 유지
t.exitonclick()