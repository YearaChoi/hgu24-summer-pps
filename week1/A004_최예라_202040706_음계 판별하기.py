scale = list(map(int,input().split()))

if scale == sorted(scale):
    print('ascending')
elif scale == sorted(scale, reverse = True):
    print('descending')
else:
    print('mixed')

# 입력받은 scale 값이 오름차순으로 정렬한 값과 같으면 ascending
# 역정렬한 값과 같으면 descending, 둘다 아니면 mixed를 출력'