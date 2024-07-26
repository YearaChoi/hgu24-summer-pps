from sys import stdin

def input():
    return stdin.readline().rstrip()

n, m = map(int, input().split())
by_id = {}
by_name = {}
for i in range(1, n + 1):
    pokemon = input()
    by_id[i] = pokemon
    by_name[pokemon] = i

for _ in range(m):
    x = input()
    if x.isdigit():
        print(by_id[int(x)])
    else:
        print(by_name[x])

# 딕셔너리 2개에 포켓몬 정보를 저장. 
# 딕셔너리 하나는 '포켓몬 번호-이름'으로, 다른 하나는 '포켓몬 이름-번호'로 매핑. 
# 찾아야 하는 것이 포켓몬 번호인지, 이름인지에 따라 각 딕셔너리에서 찾아 출력