n = int(input())
player_list = []
result = []

for _ in range(n):
    a = input()
    player_list.append(a[0])

first_names = set(player_list) # 이름 첫 글자들 집합

for i in first_names:
    if player_list.count(i) >= 5:
        result.append(i)

if len(result) > 0:
    print(''.join(sorted(result))) # 알파벳순 정렬 후 문자열 합침
else:
    print("PREDAJA")

# 모든 선수들의 이름의 첫 자리를 받아서 리스트에 저장한 뒤 set을 이용하여 중복 제거
# count를 이용하여 리스트에서 첫 자리가 5개 이상인 리스트만 따로 저장