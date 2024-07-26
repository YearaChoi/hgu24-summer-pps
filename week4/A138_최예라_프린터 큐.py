t = int(input())  # 테스트 케이스의 수

for _ in range(t):
    n, m = map(int, input().split())  # 문서의 수 n과 궁금한 문서의 위치 m을 입력 받음
    data = list(map(int, input().split()))  # 문서들의 중요도를 리스트로 입력 받음
    
    result = 1  # 출력 순서를 저장할 변수 초기화
    while data:  # 문서 리스트가 빌 때까지 반복
        if data[0] < max(data):  # 첫 번째 문서보다 중요도가 높은 문서가 있으면
            data.append(data.pop(0))  # 첫 번째 문서를 리스트의 마지막으로 이동

        else:  # 첫 번째 문서가 가장 중요도가 높은 경우
            if m == 0: break  # 궁금한 문서가 출력되는 경우 반복 종료

            data.pop(0)  # 첫 번째 문서를 출력
            result += 1  # 출력된 문서 수 증가

        m = m - 1 if m > 0 else len(data) - 1  # 궁금한 문서의 위치 갱신

    print(result)  
