n = int(input())

if n == 1:
    print('')

# 2부터 하나씩 나누기
for i in range(2, n+1):
    if n % i == 0:
    	#해당 숫자로 나눌 수 없을 때까지 나누기
        while n % i == 0:
            print(i)
            n = n / i

# 앞에 숫자에서 나눌 수 있을 만큼 나눈 다음에 다음 숫자로 넘어가야 함