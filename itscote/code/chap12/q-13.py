# 구현 문제
# p.332 Q-13 치킨 배달

from itertools import combinations

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

home = [] 
store = []  

# 집(1)과 치킨집(2)의 좌표 찾기
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            home.append((i, j))  # 집 좌표를 home 리스트에 추가
        elif city[i][j] == 2: 
            store.append((i, j))  # 치킨집 좌표를 store 리스트에 추가

# 각 집에서 가장 가까운 치킨집까지의 거리 합을 계산하는 함수
def distance(h, s):
    totalDistance = 0  
    for hx, hy in h:  
        minDistance = float('inf')  # 집에서 가장 가까운 치킨집까지의 거리 (초기값을 무한대 설정)
        for sx, sy in s:
            # 각 치킨집에 대해, 집과 치킨집 간의 거리 계산 후 최소값 갱신
            minDistance = min(minDistance, abs(hx - sx) + abs(hy - sy))
        totalDistance += minDistance  # 각 집에 대해, 해당 집에서 가장 가까운 치킨집과의 거리 총합
    return totalDistance 

# store 리스트에서 치킨집을 m개 선택할 수 있는 모든 조합
mStore = list(combinations(store, m))

result = []

for s in mStore:
    result.append(distance(home, s))  # 각 치킨집 조합에 대해 계산된 거리 합을 result 리스트에 추가

# 결과 중 가장 작은 값 선택
minDistance = min(result)
print(minDistance)
