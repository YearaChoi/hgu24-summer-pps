import math  # 수학 관련 함수를 사용하기 위해 math 모듈을 불러옵니다.

n = int(input())
for _ in range(n):
    # 두 원의 중심 좌표와 반지름을 입력받음
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    # 두 원의 중심 간의 거리를 계산 (피타고라스의 정리)
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    
    # 두 원이 동심원이고 반지름이 같을 때
    if distance == 0 and r1 == r2:
        print(-1)  # 무한히 많은 교점이 존재
    
    # 두 원이 내접하거나 외접할 때
    elif abs(r1 - r2) == distance or r1 + r2 == distance:
        print(1)  # 교점이 한 개 존재
    
    # 두 원이 서로 다른 두 점에서 만날 때
    elif abs(r1 - r2) < distance < (r1 + r2):
        print(2)  # 교점이 두 개 존재
    
    # 그 외 (두 원이 만나지 않거나 한 원이 다른 원 안에 있을 때)
    else:
        print(0)  # 교점이 없음
