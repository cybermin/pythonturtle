"""
python 예제 : 입력
"""

import turtle

# 입력
line = input("변의 길이를 입력하세요.")
# 입력된 내용은 문자열로 취급됨으로 정수로 변환
line = int(line)

# 삼각형 그리기
turtle.forward(line)
turtle.left(120)
turtle.forward(line)
turtle.left(120)
turtle.forward(line)
turtle.left(120)

# 화면 유지
turtle.exitonclick()