N = int(input())
a = int(input())
if N <= 5:
    for i in range(N-1):
        a = int(not a)
        print(a)
else:
    print("Love is open door")

# N이 5보다 크면 무조건 탈출이 불가능

# int(not a): a의 값을 반전. 0이면 1로, 1이면 0으로 변환