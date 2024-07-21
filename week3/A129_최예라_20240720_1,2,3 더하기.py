import sys

# 빠른 입력을 위해 sys.stdin.readline을 input으로 지정
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())

    # 크기가 N+1인 dp 리스트를 0으로 초기화
    dp = [0] * (N + 1)

    # 1부터 N까지 dp 값을 채움
    for i in range(1, N + 1):
        if i == 1:
            # N이 1일 때, 경우의 수는 1가지
            dp[i] = 1
        elif i == 2:
            # N이 2일 때, 경우의 수는 2가지
            dp[i] = 2
        elif i == 3:
            # N이 3일 때, 경우의 수는 4가지
            dp[i] = 4
        else:
            # N이 4 이상일 때, 점화식을 사용하여 경우의 수를 계산
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    # N에 해당하는 경우의 수를 출력
    print(dp[N])
