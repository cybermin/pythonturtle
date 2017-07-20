"""
  키보드로 거북이 움직이기
  리스트를 이용하여 거북이 색 변경
"""
import turtle as t
import random

# 오른쪽 방향키
def move_right():
    selectcolor()
    t.up()
    t.setheading(0)
    t.forward(20)
    t.down()

# 위쪽 방향키
def move_up():
    selectcolor()
    t.up()
    t.setheading(90)
    t.forward(20)
    t.down()

# 왼쪽 방향키
def move_left():
    selectcolor()
    t.up()
    t.setheading(180)
    t.forward(20)
    t.down()

# 아래쪽 방향키
def move_down():
    selectcolor()
    t.up()
    t.setheading(270)
    t.forward(20)
    t.down()

def selectcolor():
    # 거북이 색 저장 리스트
    colors = ["red","green","blue","orange","purple","pink","yellow"]
    # 색 리스트에서 랜덤으로 색 선택
    color = random.choice(colors)
    t.color(color)

# 거북이 모양
t.shape("turtle")

#키보드 처리
t.onkeypress(move_up, "Up")
t.onkeypress(move_down, "Down")
t.onkeypress(move_left, "Left")
t.onkeypress(move_right, "Right")
t.listen()


t.exitonclick()