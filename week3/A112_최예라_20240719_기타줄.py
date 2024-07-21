n,m = map(int,input().split(' '))

s = list()
o = list()

for _ in range(m):
    a,b = input().split(' ')
    s.append(int(a))
    o.append(int(b))

s = min(s)
o = min(o)

if s < o * 6:
    if s < (n % 6) * o:
        print((n // 6) * s + s)
    else:
        print((n // 6) * s + (n % 6) * o)

elif s >= o * 6:
    print(n * o)

# map() 을 사용하여 개수와 브랜드를 int로 저장
# 세트 가격을 s, 하나 당 가격을 o 에 리스트 형식으로 저장
# min() 을 이용하여 가장 작은 값을 도출
# 세트는 6개이기 때문에 가격 비교를 위하여 6개를 기준으로 잡음
# 세트가 더 싼 경우 (n // 6) * s + s,
# 낱개가 더 저렴한 경우 (n // 6) * s + (n % 6) * o,
# 낱개 6개 가격이 패키지랑 같거나 더 저렴한 경우 n * s 로 계산
