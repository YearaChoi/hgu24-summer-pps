import sys
input = sys.stdin.readline

n = int(input())
sell = {}

for i in range(n):
    name = input()
    if name not in sell:
        sell[name] = 1
    else:
        sell[name] += 1
        
max_value = max(sell.values())

best = []
for key, value in sell.items():
    if value == max_value:
        best.append(key)

best = sorted(best)
print(best[0])

# 딕셔너리를 사용

# 책 이름을 key값으로 팔린 개수를 value로, value 중에 가장 큰 값을 찾고 

# max_value를 가지는 key들을 best 리스트로 저장하여 오름차순으로 정렬하여 가장 첫 번째 책 이름을 출력