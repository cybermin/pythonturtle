"""
 구구단 출력
"""

def gugu():
    global dan
    dan = dan + 1
    for i in range(1, 10):
        print(str(dan) + " x " + str(i)+ " = " + str(dan*i))

dan = 2
gugu()

