"""
 다각형 그리기
"""

import turtle as t

# 다각형 그리기
def polygon(n, d):
    for i in range(n):
        t.forward(d)
        t.left(360 / n)

# 이동하기
def move(x,y):
    t.up()
    t.setpos(x,y)
    t.down()

n = input("n 각형을 입력세요.")
n = int(n)

d = input("변의 길이를 입력하세요.")
d = int(d)

move(-100,-100)
polygon(n, d)

t.exitonclick()