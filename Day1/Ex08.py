"""
python 예제 : 미로 그리기
"""

import turtle

# 입력
n = input("숫자를 입력하세요.")
n = int(n)

line = 10

# 다각형 그리기
turtle.shape("turtle")
for i in range(n):
    if i % 3 == 0 :
        turtle.color("red")
    elif i % 3 == 1 :
        turtle.color("blue")
    else :
        turtle.color("green")

    turtle.forward(line)
    turtle.left(90)
    line = line + 10

# 화면 유지
turtle.exitonclick()