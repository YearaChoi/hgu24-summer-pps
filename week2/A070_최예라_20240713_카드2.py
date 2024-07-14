import sys
from collections import deque
input = sys.stdin.readline

# 입력, 카드 생성
n = int(input())
cards = deque([i for i in range(1,n+1)])

# 마지막 카드가 남을 때까지 반복
while len(cards) > 1:
    # 제일 위에 있는 카드를 버린다
    cards.popleft()
    # 그 다음, 제일 위에 있는 카드를
    card = cards.popleft()
    # 제일 아래에 있는 카드 밑으로 옮긴다.
    cards.append(card)
    
# 남게 되는 카드 번호 출력
print(cards[0])

# queue 와 deque 사용

# deque 자료구조를 사용하여 카드를 처리. 
# 입력으로 n을 받고, 1부터 n까지의 숫자를 가지고 있는 deque를 생성
# while 루프에서는 마지막에 남는 카드가 1장이 될 때까지 반복
# 이때, deque의 popleft() 메소드를 사용하여 제일 위에 있는 카드를 버리고 그 다음 제일 위에 있는 카드를 변수 card에 저장
# 마지막으로, append() 메소드를 사용하여 제일 아래에 있는 카드로 옮김. 
# while 루프를 빠져나오면, 마지막으로 남은 카드의 번호를 출력. 이때, deque의 첫 번째 원소를 가져오면 됨.
# n개의 카드가 있을 때, n-1번의 반복문을 실행 -> 시간복잡도 O(n) 