import sys
input = sys.stdin.readline

N = int(input()) # 멀티탭 갯수

total = 0 # 콘센트를 꼽을 수 있는 갯수
for _ in range(N):
    total += int(input())
    
print(total - (N - 1))

