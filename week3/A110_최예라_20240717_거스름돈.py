import sys
input = sys.stdin.readline

N = int(input())
rest = 1000 - N
moneys = [500, 100, 50, 10, 5, 1]
result = 0

for money in moneys:
    if rest == 0:
        break
    
    result += rest // money
    rest %= money
    
print(result)

# 잔돈의 개수가 최대가 되도록 거스름돈을 받으려면, 액수가 큰 지폐를 최대한 많이 사용하면 됨
# 500부터 내림차순으로 지폐를 돌면서, 거스름돈을 나눈 몫을 결과값에 더하고, 거슬러준만큼 거스름돈에서 빼주는 것을 for로 반복