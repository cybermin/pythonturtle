"""
  키보드로 거북이 움직이기
  리스트를 이용하여 거북이 색 변경
"""
import turtle as t
import random

ps = 5

# 오른쪽 방향키
def move_right():
    selectcolor()
    t.up()
    t.setheading(0)
    t.forward(20)
    t.down()
    check()

# 위쪽 방향키
def move_up():
    selectcolor()
    t.up()
    t.setheading(90)
    t.forward(20)
    t.down()
    check()

# 왼쪽 방향키
def move_left():
    selectcolor()
    t.up()
    t.setheading(180)
    t.forward(20)
    t.down()
    check()

# 아래쪽 방향키
def move_down():
    selectcolor()
    t.up()
    t.setheading(270)
    t.forward(20)
    t.down()
    check()

# 먹이 이동
def move_tcircle():
    global ps
    ps = ps - 1
    if ps < 1:
        t.reset()
        tcircle.reset()
        ps = 5
        t.write("Game Over!!", False, "center", ("", 50))
    else:
        tcircle.turtlesize(ps)
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        tcircle.up()
        tcircle.setpos(x, y)
        tcircle.down()
        tcircle.write(ps)

# 먹이 먹기
def check():
    global ps
    if t.distance(tcircle) <= (15 + ps):
        tcircle.color(color)
        move_tcircle()

# 색 선택
def selectcolor():
    # 거북이 색 저장 리스트
    colors = ["red","green","blue","orange","purple","pink","yellow"]
    # 색 리스트에서 랜덤으로 색 선택
    global color
    color = random.choice(colors)
    t.color(color)

# 새로 시작
def restart():
    t.clear()
    move_tcircle()

# 거북이 모양
t.shape("turtle")

# 먹이 추가
tcircle = t.Turtle()
tcircle.shape("circle")
move_tcircle()

#키보드 처리
t.onkeypress(move_up, "Up")
t.onkeypress(move_down, "Down")
t.onkeypress(move_left, "Left")
t.onkeypress(move_right, "Right")
t.onkeypress(restart, "space")
t.listen()








t.exitonclick()