n = int(input())
array = list(map(int, input().split()))

d = [0] * n
d[0] = array[0]
for i in range(1, n):
    d[i] = max(array[i], d[i-1]+array[i])
print(max(d))

# 각 원소 i마다 그 앞의 부분합을 구할 필요 없음
# 음수가 포함되면 최댓값이 아니므로 i 직전 원소와의 합만 확인하면 됨