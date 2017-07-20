"""
python 예제 : 반복해서 원 그리기
"""

import turtle as t

# 입력
n = input("숫자를 입력하세요.")
n = int(n)

t.bgcolor("black")  # 화면 배경색 변경
t.color("yellow")   # 펜 색 지정
t.speed(0)           # 속도 지정 : 가장 빠르게

# 원 그리기
r=80                # 원의 반지름
for i in range(n):
    t.circle(r)
    t.left(360/n)

# 화면 유지
t.exitonclick()