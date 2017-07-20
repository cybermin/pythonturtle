"""
 python 함수
"""
import turtle as t

# 사각형 그리기
def square(d):
    for i in range(4):
        t.forward(d)
        t.left(90)
# 삼각형 그리기
def triangle(d):
    for i in range(3):
        t.forward(d)
        t.left(120)

# 특정위치로 이동
def init():
    t.up()
    t.setpos(-300, -100)
    t.down()

# 특정 거리만큼 이동
def move(d):
    t.up()
    t.forward(d)
    t.down()

init()
for i in range(1, 5):
    d = i * 50
    square(d)
    triangle(d)
    move(d)

t.exitonclick()

