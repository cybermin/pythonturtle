"""
  키보드로 거북이 움직이기
"""
import turtle as t
import random

# 오른쪽 방향키
def move_right():
    t.up()
    t.color(random.choice(colors))
    t.setheading(0)
    t.forward(20)
    t.down()

# 위쪽 방향키
def move_up():
    t.up()
    t.color(random.choice(colors))
    t.setheading(90)
    t.forward(20)
    t.down()

# 왼쪽 방향키
def move_left():
    t.up()
    t.color(random.choice(colors))
    t.setheading(180)
    t.forward(20)
    t.down()

# 아래쪽 방향키
def move_down():
    t.up()
    t.color(random.choice(colors))
    t.setheading(270)
    t.forward(20)
    t.down()

# 거북이 색 선택
colors = ["red", "blue", "green", "yellow", "orange"]

# 거북이 모양
t.shape("turtle")

#키보드 처리
t.onkeypress(move_up, "Up")
t.onkeypress(move_down, "Down")
t.onkeypress(move_left, "Left")
t.onkeypress(move_right, "Right")
t.listen()

t.exitonclick()