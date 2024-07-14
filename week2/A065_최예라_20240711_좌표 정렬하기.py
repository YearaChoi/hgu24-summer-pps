import sys
n=int(sys.stdin.readline())
li=[]
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    li.append([a, b])
li.sort()
for i in li:
    print(i[0], i[1])

# 이중 리스트로 모두 저장한 후 정렬
# 기본적으로 sort 함수는 오름차순으로, 앞 순서부터 정렬을 하기 때문에 sort 정렬을 사용
