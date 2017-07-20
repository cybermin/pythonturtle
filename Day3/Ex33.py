"""
 구구단 출력
"""

def gugu():
    global dan
    for i in range(1, 10):
        print(str(dan) + " x " + str(i)+ " = " + str(dan*i))

while True:
    dan = input("단 입력(종료 : 0) : ")
    dan = int(dan)

    if dan == 0:
        print("프로그램 종료")
        break
    elif dan < 2 or dan > 9:
        print("입력오류")
        continue
    else:
        gugu()



