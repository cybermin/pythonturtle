"""
총알
"""

import turtle as t
import random

def move_key(angle):
    t.up()
    t.setheading(angle)
    t.forward(15)
    t.down

def mright():
    move_key(0)

def mleft():
    move_key(180)

def mv():
    tcircle.color("red")
    tcircle.up()
    tcircle.hideturtle()
    tcircle.setpos(random.randint(-200, 200), 200)
    tcircle.showturtle()

def mup():
    temp = t.Turtle()
    temp.hideturtle()
    temp.setheading(90)
    t.setheading(90)
    x = t.xcor()
    y = t.ycor()
    temp.up()
    while True:
        if y > 250 :
            temp.reset()
            temp.hideturtle()
            break

        # if abs(tcircle.xcor - temp.xcor) < 10 and abs(tcircle.ycor - temp.ycor) < 10:
        if tcircle.distance(temp) < 20 :
            temp.reset()
            temp.hideturtle()
            tcircle.reset()
            mv()
            break

        temp.showturtle()
        temp.setpos(x, y)
        y = y + 50


tcircle = t.Turtle()
tcircle.shape("circle")

mv()

t.shape("turtle")
t.onkeypress(mright, "Right")
t.onkeypress(mleft, "Left")
t.onkeypress(mup, "space")
t.listen()

t.exitonclick()

