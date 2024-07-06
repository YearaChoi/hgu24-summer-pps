a = int(input())
b = int(input())
c = int(input())
result = list(str(a*b*c))

for i in range(10):
    print(result.count(str(i)))

# a,b,c를 각각 입력받아 곱한 값을 문자열(str)로 변환한 후 list[]로 묶는다.

# 0~9까지 for문을 돌며 i를 문자열로 바꿔 count한다. (count 함수를 사용하기 위해 정수를 문자열로 변환)