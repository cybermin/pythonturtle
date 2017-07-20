"""
  키보드로 거북이 움직이기
  리스트를 이용하여 거북이 색 변경
"""
import turtle as t
import random


# 오른쪽 방향키
def move_right():
    if playing:
        selectcolor()
        t.up()
        t.setheading(0)
        t.forward(20)
        t.down()
        check()

# 위쪽 방향키
def move_up():
    if playing:
        selectcolor()
        t.up()
        t.setheading(90)
        t.forward(20)
        t.down()
        check()

# 왼쪽 방향키
def move_left():
    if playing:
        selectcolor()
        t.up()
        t.setheading(180)
        t.forward(20)
        t.down()
        check()

# 아래쪽 방향키
def move_down():
    if playing:
        selectcolor()
        t.up()
        t.setheading(270)
        t.forward(20)
        t.down()
        check()

# 먹이 이동
def move_tcircle():
    for i in range(10):
        tcircles.append(t.Turtle())
    for tcircle in tcircles:
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        tcircle.up()
        tcircle.setpos(x, y)
        tcircle.down()

# 먹이 먹기
def check():
    for tcircle in tcircles:
        if t.distance(tcircle) <= 12:
            tcircle.hideturtle()
            tcircles.remove(tcircle)
            break

    if len(tcircles) == 0:
        t.write("Game Over!!", False, "center", ("", 50))
        global playing
        playing = False

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
    playing = True
    t.clear()
    move_tcircle()

# 게임 시작
playing = True

# 거북이 모양
t.shape("turtle")

# 먹이 추가
tcircles = []
move_tcircle()

#키보드 처리
t.onkeypress(move_up, "Up")
t.onkeypress(move_down, "Down")
t.onkeypress(move_left, "Left")
t.onkeypress(move_right, "Right")
t.onkeypress(restart, "space")
t.listen()


t.exitonclick()