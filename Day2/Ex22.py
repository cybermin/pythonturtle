"""
python 예제 : 튜플
"""

import turtle as t

colors = ("red", "blue", "green", "orange")

t.shape("turtle")
t.up()
t.setpos(-200, 0)

for color in colors:
    t.up()
    t.color(color)
    t.forward(100)
    t.stamp()

# 화면 유지
t.exitonclick()