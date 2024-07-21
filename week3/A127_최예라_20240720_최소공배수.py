import sys

T = int(input())

for i in range(T):
    # 표준 입력으로부터 두 정수 a와 b를 입력
    a, b = map(int, sys.stdin.readline().split())
    
    # 원래의 a와 b 값을 보존
    aa, bb = a, b

    # 유클리드 호제법을 이용해 최대공약수를 구함
    # a % b가 0이 될 때까지 반복
    while a % b != 0:
        # a와 b의 값을 변경 (a는 b로, b는 a % b로)
        a, b = b, a % b

    # 최소공배수를 출력
    # aa * bb는 a와 b의 곱이고, b는 최대공약수
    # 최소공배수는 두 수의 곱을 최대공약수로 나눈 값
    print(aa * bb // b)
