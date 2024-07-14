x = input()
y = ''
for i in x:
    if i in 'ABC':
        y += chr(ord(i) +23)
    else:
        y += chr(ord(i) - 3)
print(y)

# 아스키 코드(ord,chr)활용
# ABC를 제외한 문자는 모두 3칸씩 뒤로 밀린 알파벳을 출력
# ABC는 +23칸