import sys
n = int(sys.stdin.readline())

stack=[]
for i in range(n):
    command = sys.stdin.readline().split()

    if command[0]=='push':
        stack.append(command[1])
    elif command[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])

# 파이썬은 따로 stack 구조를 제공하지 않음 -> 기본 클래스 list를 이용하여 stack 표현

# input() 함수를 사용할 경우, 시간초과 에러가 뜨므로 시간단축을 위해 sys.stdin.readline()을 사용
# 입출력 속도 : sys.stdin.readline > raw_input() > input()