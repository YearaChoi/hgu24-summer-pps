N, K = int(input()), int(input())

# 이분 탐색을 위한 초기 범위 설정
start, end = 1, K

# 이분 탐색 시작
while start <= end:
    mid = (start + end) // 2  # 중간 값 계산
    
    # mid 이하의 숫자가 몇 개 있는지 계산하기 위한 변수 temp 초기화
    temp = 0
    for i in range(1, N+1):
        # mid 이하의 i의 배수의 수를 더한다. 단, N보다 클 수 없음
        temp += min(mid // i, N)
    
    if temp >= K:  # K번째 수가 mid보다 작거나 같다면
        answer = mid  # 현재 mid 값을 잠정적인 답으로 저장
        end = mid - 1  
    else:
        start = mid + 1  # K번째 수가 mid보다 크다면, 더 큰 값을 찾기 위해 범위를 늘림

print(answer)
