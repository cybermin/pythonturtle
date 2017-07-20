"""
랜덤으로 거북이 이동
"""
# 사용 모듈 추가
import turtle as t
import random as rand

# 입력
n = input("이동할 횟수를 입력하세요.")
n = int(n)

# 화면 세팅
t.reset()
t.shape("turtle")
t.speed(0)
t.bgcolor("black")
t.color("yellow")

# n번 반복
for i in range(n):
    angle = rand.randint(1, 360)
    t.setheading(angle)

    d = rand.randint(1,20)
    t.forward(d)

t.exitonclick()

