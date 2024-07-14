num = int(input())
line = 1

while num > line:
    num -= line
    line += 1
    
# 짝수 경우
if line % 2 == 0:
    a = num
    b = line - num + 1

# 홀수 경우
elif line % 2 == 1:
    a = line - num + 1
    b = num

print(f'{a}/{b}')

# 짝수 라인 : 분모가 1씩 늘어나고 분자가 1씩 줄어듦
# 홀수 라인 : 분자가 1씩 늘어나고 분모가 1씩 줄어듦

# line - num + 1: 대각선에서 분수의 위치에 따라서 분자 또는 분모를 계산하기 위해 사용되는 식, 이 값이 a이냐 b이냐에 따라 분자와 분모를 결정