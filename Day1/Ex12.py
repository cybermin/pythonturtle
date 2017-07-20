"""
 무한 루프 예제
"""

# 무한루프
while True:
    # 입력
    n = input("정수를 입력하세요.(종료 : 0) ")

    # 입력된 값을 정수로 변환
    n = int(n)

    # 입력된 값이 0이면 무한 루프를 종료
    if n == 0:
        break

    # 입력된 값 짝/홀 구분
    if n % 2 == 0:
        print(str(n) + "은 짝수입니다")
    else:
        print(str(n) + "은 홀수입니다")

