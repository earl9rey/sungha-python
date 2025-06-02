# DFS/BFS
# p.351 Q-20 감시 피하기 

import copy
from itertools import combinations

n = int(input())
passage = [list(map(str, input().split())) for _ in range(n)]

empty = [(i, j) for i in range(n) for j in range(n) if passage[i][j] == "X"] 
threeblock = list(combinations(empty, 3))

evade = False

def check_evade(graph, x, y) : # 감시를 피할 수 있는지 여부를 판단하는 함수
    global evade
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4) : # 상하좌우 모든 방향에 대해서
        nx, ny = x, y
        while 0 <= nx < n and 0 <= ny < n: # 벽에 닿을 때까지 이동 
            nx += dx[i]
            ny += dy[i]
            if not (0 <= nx < n and 0 <= ny < n): # 벽에 닿으면 (범위 벗어나면) 종료
                break  
            if graph[nx][ny] == "S": # 학생이 보이면 감시 피하기 실패 (False)
                evade = False 
                return
            elif graph[nx][ny] == "O": # 장애물 만나면 감시 불가 (다음 방향 확인)
                break               

for blocks in threeblock: # 각 모든 조합에 대해 검사하기
    result = copy.deepcopy(passage) # 감시 체크용 복사본

    for x, y in blocks: # 장애물을 만들 위치 조합에 대해
        result[x][y] = "O" # 그 위치의 빈칸에 장애물 세우기

    evade = True

    for i in range(n):
        for j in range(n):
            if result[i][j] == "T" : 
                check_evade(result, i, j) # 감시 성공 여부 확인
    
    if evade: # 한 번이라도 감시 피하기를 실패했다면 (학생이 들켰다면)
        break  

if evade==True :
    print("YES")
else :
    print("NO")