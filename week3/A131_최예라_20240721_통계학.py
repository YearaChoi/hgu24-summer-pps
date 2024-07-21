import sys
input=sys.stdin.readline

n=int(input())
arr=[]

for i in range(n):
    arr.append(int(input()))

arr.sort() #중앙값을 구하기 위해 정렬

print(round(sum(arr)/len(arr))) #1) 산술평균
print(arr[len(arr)//2]) #2) 중앙값

#최빈값
dic=dict()
for i in arr: #빈도수 구하기
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
        
mx=max(dic.values()) #빈도수 중 최대값 구하기
mx_dic=[] #최빈값 숫자를 저장할 배열

for i in dic: #빈도수 딕셔너리에서
    if mx==dic[i]: #최빈값의 key저장
        mx_dic.append(i)

if len(mx_dic)>1: #최빈값이 여러개라면
    print(mx_dic[1]) #두번째로 작은 값  3)최빈값
else: #하나라면
    print(mx_dic[0]) #해당 값 출력  3)최빈값
    
print(max(arr)-min(arr)) #4) 범위

# 문제에서 산술평균은 반올림을 해주어야 하므로, round 사용
# 중앙값을 구하기 위해 입력받은 숫자를 정렬
# 최빈값을 구하기 위해 딕셔너리 사용. 딕셔너리를 사용해 각 숫자의 빈도를 구함
# 빈도 중 최댓값(최빈값)을 갖는 값을 변수에 저장
# 이후 최빈값의 key값을 빈 배열(mx_dic)에 추가하고, 최빈값이 여러개인지 아닌지에 따라 값을 출력
# 마지막으로 범위는 최댓값과 최솟값의 차이이므로 max와 min을 사용