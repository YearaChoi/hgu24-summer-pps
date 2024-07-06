num = map(int,input().split())

vnum = 0
for i in num:
    vnum += i**2

print(vnum%10)

# num으로 값을 받는다.

# 반복문으로 제곱한 수의 합을 vnum에 저장

# 각 숫자를 제곱한 수들의 합을 10으로 나눈 나머지를 출력

# for i in num: num의 각 요소를 순회
# for i in range(num): 0부터 num-1까지의 정수를 생성하여 순회