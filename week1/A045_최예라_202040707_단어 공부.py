word = input().upper()
word_list = list(set(word))
arr = []

for i in word_list:
    count = word.count(i)
    arr.append(count)

if arr.count(max(arr))>= 2:
    print("?")
else:
    print(word_list[arr.index(max(arr))])

# set함수로 문자열 내 중복문자를 제거하고 리스트로 변환
# 중복문자를 제거한 배열을 for문을 돌며, count 함수를 통해 입력받은 문자열 내 알파벳 개수를 빈 리스트에 입력