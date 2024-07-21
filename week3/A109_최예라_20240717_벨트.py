import sys
input = sys.stdin.readline

m = int(input()) # 벨트 종류의 개수
ans = 0 # 마지막 바퀴의 분당 회전수
rot = 0 # 마지막 바퀴의 회전방향

for i in range(m):
    a, b, r = map(int,input().split())
    if(i == 0): ans = a * b
    else: ans = int(ans / a * b)
    if(r == 1): rot = 1 - rot
    
print(rot,ans)

# i번째 바퀴를 a, i+1번째 바퀴를 b, 그 때의 회전 방향을 r이라고 가정해 변수를 선언해주어 m만큼 입력받음

# 1번째 바퀴 * 2번째 바퀴가 2번째 바퀴의 회전 수
#  이후 i번째 바퀴가 ans / a * b만큼 돌게 됨 
# 매 입력마다 r이 1이라면 방향이 반대가 되기 때문에 rot 값을 toggle.