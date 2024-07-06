people_nums = []
people = 0

for _ in range(4):
    out_num, in_num = map(int, input().split())
    people += in_num
    people -= out_num
    
    people_nums.append(people)
    
print(max(people_nums))

# 사용자에게 정수를 입력받아 각각 out_num, in_num에 저장
# 현재 버스에 남아있는 사람 수 (people)를 people_nums 리스트에 추가

# people_nums 리스트에서 가장 큰 값을 출력