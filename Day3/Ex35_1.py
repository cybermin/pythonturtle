"""
timer 동작
"""

import turtle as t
import random


def move_key(angle):
    t.up()
    t.setheading(angle)
    t.forward(15)
    t.down
    check()

def mright():
    move_key(0)

def mup():
    move_key(90)

def mleft():
    move_key(180)

def mdown():
    move_key(270)

def movet1():
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)

    t1.up()
    t1.setpos(x,y)
    t1.showturtle()

def check():
    if t.distance(t1) < 10:
        global total
        tw.up()
        tw.hideturtle()
        tw.setpos(250, 250)
        total = total + 1
        tw.clear()
        tw.write("Count:" + str(total), False, "center", ("", 20))
        t1.clear()
        movet1()


def movetimer():
    global tm
    tTimer.up()
    tTimer.hideturtle()
    tTimer.setpos(250, 280)
    tTimer.clear()
    tTimer.write("Timer:" + str(tm), False, "center", ("", 20))
    tm = tm + 1
    if tm % 5 == 0 : movet1()
    t.ontimer(movetimer, 1000)


tTimer = t.Turtle()
tTimer.hideturtle()
tm = 0
tw = t.Turtle()
tw.hideturtle()
total = 0

t1 = t.Turtle()
t1.shape("circle")
t1.color("red")
playing = True
t1.hideturtle()

t.shape("turtle")

movetimer()

t.onkeypress(mup, "Up")
t.onkeypress(mdown, "Down")
t.onkeypress(mleft, "Left")
t.onkeypress(mright, "Right")
t.listen()

t.exitonclick()