# 풀이1
num1 = int(input())
num2 = int(input())

# 나머지를 구하는 %을 이용하여 값을 바로 출력
print(num1 * (num2%10))
print(num1 * ((num2%100)//10))
print(num1 * (num2//100))
print(num1 * num2)

# 풀이2
num1 = int(input())
num2 = input() 

# range(시작, 마지막, 순서) 함수를 이용해 마지막부터 시작까지 역순으로 출력
for i in range(len(num2), 0, -1):	
    print(num1 * int(num2[i-1]))

print(num1 * int(num2))