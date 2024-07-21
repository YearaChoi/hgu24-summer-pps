n = int(input())

for i in range(n):
    a = input()
    b = a[::-1]
    sum = str(int(a) + int(b))
    if (sum == sum[::-1]):
        print("YES")
    else:
        print("NO")

# 문자열 뒤집기: a[::-1] index를 -1를 지정

