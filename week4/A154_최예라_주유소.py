n=int(input()) #도시의 개수
km=list(map(int,input().split())) #도로의 길이
price=list(map(int,input().split())) #가격

minPrice=price[0] # 임의의 가격 값을 지정
total=0 # 비용을 저장할 변수

# 최소값을 구하는 반복문
# 가격은 도시 수(n)만큼 존재하고, 최종 목적지에서는 기름을 더이상 충전하지 않아도 되므로 총 n-1번 반복
for i in range(n-1): 
    if minPrice>price[i]: # 기름의 최저가
        minPrice=price[i]

    total+=(minPrice*km[i]) # 총 가격
print(total)

# 가격을 최소화하기 위해 가장 싼 곳에서 가장 많이 구매해야하므로, 가격의 최솟값을 찾아야 함.
# 가장 싼 곳에서 가야할 km만큼의 기름을 구매하고, 이를 비용에 더해준다.

