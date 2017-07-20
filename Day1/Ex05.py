"""
python 예제 : N각형 그리기
"""

import turtle

# 입력
line = input("변의 길이를 입력하세요.")
# 입력된 내용은 문자열로 취급됨으로 정수로 변환
line = int(line)

n = input("n 각형의 n을 입력하세요.")
n = int(n)

# 다각형 그리기
for i in range(n):
    turtle.forward(line)
    turtle.left(360/n)

# 화면 유지
turtle.exitonclick()