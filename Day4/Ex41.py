"""
 Turtle 화면 좌표 정하기
"""

import turtle as t
import random

# 화면의 좌표를 (0,0)에서 (300,300)으로 설정
def turtleScreen():
    t.setworldcoordinates(0,0,300,300)
    t.reset()

# 포인트 이동
def move(x, y):
    t.up()
    t.setpos(x,y)
    t.down()

# 화면을 9등분으로 나누기
def gridDraw():
    t.hideturtle()
    t.speed(0)
    t.setheading(0)
    for i in range(5):
        move(0, i * 100)
        t.forward(300)

    t.setheading(90)
    for i in range(5):
        move(i * 100,0)
        t.forward(300)

# 마우스를  누른 위치의 인덱스 추출
def getIndex(x,y):
    if (0 < x < 100) and (200 < y < 300):
        idx = 0
    elif (100 < x < 200) and (200 < y < 300):
        idx = 1
    elif (200 < x < 300) and (200 < y < 300):
        idx = 2
    elif (0 < x < 100) and (100 < y < 200):
        idx = 3
    elif (100 < x < 200) and (100 < y < 200):
        idx = 4
    elif (200 < x < 300) and (100 < y < 200):
        idx = 5
    elif (0 < x < 100) and (0 < y < 100):
        idx = 6
    elif (100 < x < 200) and (0 < y < 100):
        idx = 7
    elif (200 < x < 300) and (0 < y < 100):
        idx = 8

    return idx

# 게임 진행
def play(x, y):
    idx = getIndex(x,y)
    if board[idx] == "":
        board[idx] = "O"
        move(pos[idx][0], pos[idx][1])
        t.write(board[idx],False, "center", ("",30))
        if checkwin("O"):
            return

        while True:
            comidx = random.randint(0, 8)
            if board[comidx] == "":
                board[comidx] = "X"
                move(pos[comidx][0], pos[comidx][1])
                t.write(board[comidx], False, "center", ("", 30))
                checkwin("X")
                break

# 결과 판단
def checkwin(c):
    if checkall(c):
        t.reset()
        move(150,150)
        if c == "O":
            t.write("win!!", False, "center", ("", 100))
        elif c == "X":
            t.write("out!!", False, "center", ("", 100))
        move(120, 100)
        t.write("Press Space....", False, "center", ("", 50))

# 해당 라인이 같은 문자로 채워졌는지 확인
def checkline(c, x, y, z):
    if (board[x] == c and board[y] == c and board[z] == c):
        return True
    else:
        return False

# 이길수 있는 모든 라인 체크
def checkall(c):
    if checkline(c, 0, 1, 2):
        return True
    elif checkline(c, 3, 4, 5):
        return True
    elif checkline(c, 6, 7, 8):
        return True
    elif checkline(c, 0, 3, 6):
        return True
    elif checkline(c, 1, 4, 7):
        return True
    elif checkline(c, 2, 5, 8):
        return True
    elif checkline(c, 0, 4, 8):
        return True
    elif checkline(c, 2, 4, 6):
        return True
    else:
        return False

# 화면 초기화
def init():
    t.reset()
    gridDraw()
    for i in range(len(board)):
        board[i] = ""


pos = [[50,250], [150,250], [250,250],
       [50, 150], [150, 150], [250, 150],
       [50, 50], [150, 50], [250, 50]]
board = ["", "", "",
         "", "", "",
         "", "", ""]

turtleScreen()
gridDraw()
t.onscreenclick(play)

t.onkeypress(init, "space")
t.listen()

t.mainloop()