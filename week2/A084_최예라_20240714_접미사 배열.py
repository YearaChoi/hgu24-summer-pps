s = input()
answer = []

# 입력받은 input() 문자열의 길이만큼 반복
# 맨 앞글 자의 순서를 제외하고 나머지 뒤의 문자열을 append
for i in range(len(s)): 
    answer.append(s[i:])

answer.sort()

# 알파벳순 정렬
for i in answer:
    print(i)