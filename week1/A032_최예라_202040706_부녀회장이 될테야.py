t = int(input())

for _ in range(t):  
    k = int(input())  # 층
    n = int(input())  # 호
    k0 = [x for x in range(1, n+1)]  # 0층 리스트
    for k in range(k):  # 층 수 만큼 반복
        for i in range(1, n):  # 1 ~ n-1까지 (인덱스로 사용)
            k0[i] += k0[i-1]  # 층별 각 호실의 사람 수를 변경
    print(k0[-1])  # 가장 마지막 수 출력