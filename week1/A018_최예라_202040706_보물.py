num = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
s = 0
for i in range(num):
    b_max = max(b)
    s+= a[i] * b_max
    b.remove(b_max)
    
print(s)

# A를 오름차순으로 정렬
# B에서 가장 큰 수와 A에서 가장 작은 수를 곱한 값을 S에 더한다.
# b를 pop한다.