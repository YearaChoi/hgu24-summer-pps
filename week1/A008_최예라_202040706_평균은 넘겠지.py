num = int(input())

for _ in range(num):
    scores = list(map(int,input().split()))
    avg = sum(scores[1:])/scores[0]
    
    cnt = 0
    for i in scores[1:]:
        if i > avg:
            cnt +=1
    per = (cnt/scores[0])*100
    print('%.3f' %per + '%')

# num에 테스트 케이스 개수를 입력받아 저장

# 테스트 개수의 개수만큼 for문을 반복
# scores에 list의 형태로 학생의 수, 학생들의 점수를 저장
# input.split()을 이용하면 입력을 띄어쓰기로 구분하여 저장할 수 있다.
# 평균을 구하기 위해 1번째 요소부터 마지막 까지 sum을 이용하여 더한 다음, 학생의 수인 scores[0]으로 나눠주고 avg에 저장

# 평균을 넘는 학생의 수를 세기 위하여 cnt를 정의해준다.
# scores의 1번째 요소부터 평균이 넘는지 확인
# 평균을 넘는다면 cnt에 1을 더해준다.
# cnt을 학생의 수인 scores[0]로 나눠준 다음, 100을 곱해준다.

# %.3f를 하여 per의 소수점 3번째짜리 까지만 출력

