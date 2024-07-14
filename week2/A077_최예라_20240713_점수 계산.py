li = []
for _ in range(8):
    li.append(int(input()))
res = sorted(li)[3:]
tmp = []
print(sum(res))
for i in res:
    tmp.append(li.index(i)+1)
print(*sorted(tmp))

# 값들 중 큰 값 5개를 list에 넣고 tmp에 해당 값들을 넣고 최초 List로부터 기존의 index를 빼냄