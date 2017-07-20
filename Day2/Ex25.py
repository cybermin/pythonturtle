"""
python 예제 : 영어 단어 게임
"""
import random

print("*** 영어 단어 게임 ***")
fruits = ["사과", "바나나", "오렌지"]
efruits = ["apple", "banana", "orange"]

total = 0
ocnt = 0
while True:
    fruit = random.choice(fruits)
    idx = fruits.index(fruit)
    print("Q:" + fruit)
    ans = input("영어단어 입력 (종료 exit): ")

    if ans == "exit":
       print("프로그램 종료")
       break

    total = total + 1
    if ans == efruits[idx]:
        print("[맞음 !!]")
        ocnt = ocnt + 1
    else:
        print("[틀림 !!]")

print("전체 횟수 : " + str(total))
print("맞은 횟수 : " + str(ocnt))