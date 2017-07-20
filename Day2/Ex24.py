"""
python 예제 : 리스트 함수 정리
"""
import random

list = [1,5,2,4,3,6]

print(random.choice(list))  # 리스트에서 랜덤 자료 추출
print(list.index(4))        # 리스트의 해당 자료 index

list.append(7)              # 마지막에 자료 추가
print(list)                 # 리스트 내용 출력

list.pop()                  # 리스트 마지막 자료 삭제
list.reverse()              # 리스트 뒤집기
list.sort()                 #리스트 정렬
list.remove(3)              #리스트 요소 제거

# 예외 처리
try:
    list.remove(3)
    print(list)
except:
    print("요소를 찾을 수 없습니다.")

