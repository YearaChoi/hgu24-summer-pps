count = int(input()) # 입력받을 스택 리스트 안의 총 숫자의 수
stack = [] # 스택 리스트

for i in range(count): 
    num = int(input())
    if(num == 0): #num이 0이면 pop
        stack.pop()
    else:
        stack.append(num) #그게 아니라면 append = push
print(sum(stack))

# stack = [] 로 배열을 생성
# 입력받은 수가 0이면 stack.pop()을 통해 전에 입력받은 값을 삭제
# 아니라면 stack.append(N)을 통해 입력받은 값을 스택 배열에 추가
# 마지막으로 배열에 담긴 수들을 sum 함수를 이용해서 더해준 뒤 출력