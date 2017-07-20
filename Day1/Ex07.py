"""
python 예제 : 홀짝 게임
"""

import random

# 랜덤수 생성
n = random.randint(1, 100)

# 사용자 입력
ans = input("홀/짝 입력 => ")

# 확인
print("발생수 : " + str(n))

"""
if n % 2 == 0 and ans == "짝":
   print("맞음!!")

if n % 2 == 1 and ans == "홀":
   print("맞음!!")

if n % 2 == 0 and ans == "홀":
   print("틀림!!")

if n % 2 == 1 and ans == "짝":
   print("틀림!!")
"""

if (n % 2 == 0 and ans == "짝") or (n % 2 == 1 and ans == "홀") :
    print("맞음!!")
else:
    print("틀림!!")