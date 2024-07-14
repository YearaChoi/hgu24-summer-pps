N = int(input())
group_word = N

for i in range(N) :
    word = input()
    for j in range(len(word)-1) :
        if word[j] == word[j+1] :
            continue
        elif word[j] in word[j+1:] :
            group_word -= 1
            break
print(group_word)

# 단어의 개수를 그룹 단어에 저장
# word를 입력받고 0번째 글자부터 for문
# 연속된 글자가 같은 글자면 continue
# 이후 글자가 같은 글자일 경우 그룹 단어가 아니므로 -1