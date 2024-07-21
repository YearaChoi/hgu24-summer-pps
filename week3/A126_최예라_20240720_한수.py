num = int(input())
hansu = 0

for n in range(1, num+1) :
    if n <= 99 : # 1부터 99까지는 모두 한수
        hansu += 1 
    
    else :     
        nums = list(map(int, str(n))) # 숫자를 자릿수대로 분리 
        if nums[0] - nums[1] == nums[1] - nums[2] : #등차수열 확인
            hansu+=1

# 123의 숫자가 있다고 하면 자릿수대로 이 숫자들을 하나씩 분리 -> 1, 2, 3의 숫자가 됨. 
# 이 숫자들은 등차수열을 이루므로 123은 한수이다. 주의할 것은 1부터 9까지도 한수에 포함한다.

# 100 미만인 수는 모두 한수. 두 자릿수의 경우 앞의 항과 뒷 항의 차가 공차가 되며, 이후 연속된 숫자가 존재하지 않기 때문

# n = int(input())
# hansu = 0
#  
# for i in range(1, n+1):
#     if i < 100:
#         hansu += 1
#     if i >= 100:
#         temp1 = int(str(i)[0]) - int(str(i)[1])
#         temp2 = int(str(i)[1]) - int(str(i)[2])
#         if  temp1 == temp2:
#             hansu+=1
#  
# print(hansu)