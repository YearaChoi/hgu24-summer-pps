n = []

for _ in range(10):
    a = int(input())
    b = a % 42
    n.append(b)

s = set(n)
print(len(s))

# 자료형의 중복을 제거하기 위한 필터 역할로 set 사용