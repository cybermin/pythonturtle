"""
 구구단 게임
"""
import random

# 결과 확인
def check(x, y, ans):
    global total, ocnt
    total = total + 1
    if x * y == ans:
        print("정답!!")
        ocnt = ocnt + 1
    else:
        print("오답!!")

# 결과 출력
def show():
    global total,ocnt
    print("총 횟수 : " + str(total))
    print("맞춘 횟수 : " + str(ocnt))
    print("승률 : " + str(round(ocnt/total, 3)))


print("**** 구구단 게임 ****")
total = 0   # 전체 게임횟수
ocnt = 0    # 맞춘 횟수
while True:
    x = random.randint(2, 9)
    y = random.randint(1, 9)

    print(str(x) + " x " + str(y))
    ans = input("입력(종료 : 0) : ")
    ans = int(ans)

    if ans == 0:
        print("프로그램 종료")
        show()
        break
    else:
        check(x, y, ans)



