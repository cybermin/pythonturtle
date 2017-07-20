"""
python 예제 : 반복문 for
"""

import turtle

# 입력
x = input("정수 입력: ")
x = int(x)

y = input("정수 입력: ")
y = int(y)

sum = 0     # 합계
cnt = 0     # 개수

for i in range(min(x,y),max(x,y)+1):
    print(i)
    sum = sum + i
    cnt = cnt + 1

print("합계: " + str(sum))
print("개수: " + str(cnt))
print("평균: " + str(round(sum/cnt, 2)))
