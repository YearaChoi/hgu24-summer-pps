num = int(input())

for i in range(num):
    ans = list(input())
    score = 0
    plus_score = 0
    for i in ans:
        if i == 'O':
            plus_score += 1
            score = score+plus_score
        elif i =='X':
            plus_score = 0
    print(score)

# list 함수를 통해 OXOX 값을 'O' 'X'로 하나하나 받음
# for문을 통해 만약 값이 O이면 값을 더하되 plus_score을 활용하여 연속득점 보너스를 추가