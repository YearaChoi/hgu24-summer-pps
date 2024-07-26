import sys
input = sys.stdin.readline

n, c = map(int,input().split())
houses = [int(input()) for i in range(n)]
houses.sort()

# 최소거리와 최대거리
start = 1
end = houses[-1] - houses[0]

def binarySearch(houses, start, end):
	# 최소 거리가 최대 거리보다 작거나 같을 때까지 반복
    while start <= end:
        mid = (start + end) // 2
        # 앞에서부터 탐색
        current = houses[0]
        cnt = 1
        for i in range(1,n):
            # 현재 위치에서 다음 집과의 거리가 mid 이상이라면
            if houses[i] >= current + mid:
                # 공유기 개수 + 1
                cnt += 1
                # 현재 위치 갱신
                current = houses[i]
        if cnt >= c:
            # cnt가 c 이상이면 더 넓게 설치 가능함
            start = mid + 1
            result = mid
        else:
            # c 미만이면 더 좁게 설치 해야함
            end = mid - 1
    return result

print(binarySearch(houses, start, end))

# 이분 탐색(이진 탐색)은 본래 정렬된 배열에서 특정 값을 찾는 알고리즘
# 가장 인접한 두 공유기 사이의 최대 거리는 최대 중간값에 해당한다.

# 집을 정렬 후, 최소 거리 ~ 최대 거리를 설정하고 중간 거리 값을 계산한다.
# 중간 거리를 기준으로 앞에서부터 공유기를 설치했을 때,
# 공유기 수가 c개 이상 설치된다면 거리를 늘린다. (설정한 거리가 좁아서 더 많이 설치된 것이므로)
# 공유기 수가 c개 미만이라면 거리를 좁힌다. (설정한 거리가 넓어서 설치를 못한 것이므로)