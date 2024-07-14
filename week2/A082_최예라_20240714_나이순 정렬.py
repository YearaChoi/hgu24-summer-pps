A=int(input())
user = []
for _ in range(A):
    age, name = input().split()
    user.append([int(age),name])

for i in sorted(user,key=lambda x : x[0]):
    print(i[0],i[1])

# sorted 함수의 key값으로 람다(lambda) 함수를 이용해 나이를 기준으로 정렬
# 파이썬에서는 정렬 기준을 함수로 지정할 수 있기 때문에, 람다 함수를 이용해 간단하게 나이를 기준으로 정렬 가능