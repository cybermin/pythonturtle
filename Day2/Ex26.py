"""
python 예제 : 주차게임
"""
import random

print("*** 주차 게임 ***")
tower = []

while True:
    menu = input("1.주차 2.출차 3.보기 0.종료 : [메뉴입력]")
    menu = int(menu)

    if menu == 1:
        num = input("[주차]차량번호 입력 : ")
        try:
            tower.index(num)
            print("주차 차량이 중복됩니다")
        except:
            tower.append(num)
            print("[+]" + num + " 주차")
    elif menu == 2:
        num = input("[출차]차량번호 입력 : ")
        # index() 함수 예외 처리
        try:
            tower.remove(num)
            print("[-]" + num + " 출차")
        except:
            print("주차 차량이 없습니다...")
    elif menu == 3:
        print(tower)
    elif menu == 0:
        print(" 프로그램 종료 ....")
        break
    else:
        print(" 메뉴 입력 오류")
