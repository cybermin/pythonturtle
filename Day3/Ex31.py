"""
  키보드로 거북이 도장 찍기
"""
import turtle as t
import random

# 도장 찍기
def show():
    x = random.randint(-300, 300)   # 랜덤 x좌표
    y = random.randint(-300, 300)   # 랜덤 y좌표
    color = random.choice(colors)   # 랜덤 색 선택
    t.showturtle()                  # 거북이 보이기
    t.up()                          # 펜을 올림
    t.color(color)
    t.turtlesize(random.randint(1,3))   # 랜덤 거북이 크기
    t.setpos(x,y)                   # 거북이 랜덤 위치
    t.stamp()                       # 도장찍기

# 거북이 색 선택
colors = ["red", "blue", "green", "yellow", "orange"]

# 거북이 모양
t.shape("turtle")
t.hideturtle()

#키보드 처리
t.onkeypress(show, "space")
t.listen()

t.exitonclick()