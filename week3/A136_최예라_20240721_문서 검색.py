word = input() # 사용자가 입력한 문자열
small = input() # 사용자가 입력한 문자열에서 찾고자하는 부분 문자열 저장
sp_word = word.split(small) # word 문자열을 small 문자열을 기준으로 분리하여 리스트로.
# word가 "banana"이고 small이 "na"인 경우, sp_word는 ["ba", "", ""]

print(len(sp_word) - 1) # small 문자열이 word에 몇 번 나타나는지
