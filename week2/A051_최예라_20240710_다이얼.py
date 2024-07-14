dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

alpha = list(input())		
result = 0

for i in alpha:
    for j in dial:
        if i in str(j):	
            num = dial.index(j) + 3		
            result += num
print(result)

# 다이얼을 리스트로 정리
# 알파벳 단어 입력받음
# 알파벳이 str(다이얼)에 있으면 해당 다이얼 Index를 구함
# 숫자 2를 걸때 3초가 걸리는 숫자 2에 해당하는 다이얼의 index는 0이므로 각 index에 + 3 을 해주면 각 알파벳 별 필요한 시간이 됨


