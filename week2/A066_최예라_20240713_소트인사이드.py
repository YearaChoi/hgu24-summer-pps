nums = list(map(int, str(input())))
nums.sort(reverse=True)
for i in nums:
    print(i,end='')

# 모든 수를 슬라이싱하여 리스트로 담음. 1234 -> [1, 2, 3, 4]
# 내림차순 정렬 (reverse = True)
# end=''를 이용하여 i를 띄어쓰기 없이 출력