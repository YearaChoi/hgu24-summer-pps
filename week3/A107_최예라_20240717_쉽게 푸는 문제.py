a,b = map(int,input().split())
 
arr = [0]
for i in range(46):
    for j in range(i):
        arr.append(i)
 
print(sum(arr[a:b+1]))

# a, b의 범위는 1,000까지였기 때문에 반복문의 범위는 46까지만 구해도 됨 (len(arr) = 1036)
# i값을 기준으로 이중 반복문을 사용하는데 빈 arr에 i를 추가. 값이 1부터 arr에 들어감 (j를 추가하는 것이 아님)
# sum함수 이용: 구간합을 구하지 않고 기존 arr에서 사용 가능
# 구간 합을 구할 때 누적 합을 구하지 않고도 sum + slicing 함수로 구할 수 있음