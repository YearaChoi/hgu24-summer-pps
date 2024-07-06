num = input()
checked = [0]*10

for i in num:
  if i == '6' or i == '9':
    if checked[6] <= checked[9]:
      checked[6] += 1
    else:
      checked[9] += 1
  else:
    checked[int(i)] += 1

print(max(checked))

# 사용자로부터 입력을 받아 문자열 num에 저장
# 길이가 10인 리스트 checked를 생성하고, 모든 요소를 0으로 초기화

# 현재 문자가 '6' 또는 '9'일 경우, checked[6]와 checked[9] 중 더 작은 값을 가지는 쪽을 증가시킴
# 현재 문자가 '6' 또는 '9'가 아닌 경우, 해당 숫자에 해당하는 checked 리스트의 요소를 증가시킴

# checked 리스트에서 가장 큰 값을 출력