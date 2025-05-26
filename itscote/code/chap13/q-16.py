# DFS/BFS
# p.341 Q-16 연구소

import copy
from itertools import combinations

n, m = map(int, input().split())
maplist = [list(map(int, input().split())) for _ in range(n)]

empty = [(i, j) for i in range(n) for j in range(m) if maplist[i][j] == 0] # 빈칸 리스트
threewall = list(combinations(empty, 3)) # 빈칸 중 3개의 벽을 세울 위치 조합
    
def dfs(graph, x, y, visited) : # 바이러스 확산 검사
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visited.append((x, y))

    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
    
        if 0 <= nx < n and 0 <= ny < m:
            if (nx, ny) not in visited and graph[nx][ny] == 0: # 아직 방문하지 않은 모든 확산 가능한 빈칸에 대해
                graph[nx][ny] = 2 # 바이러스 확산 처리
                dfs(graph, nx, ny, visited)


max_safe = 0

for walls in threewall: # 각 모든 조합에 대해 검사하기
    visited = []
    resultlist = copy.deepcopy(maplist) # 확산 체크용 지도

    for x, y in walls: # 벽을 만들 위치 조합에 대해
        resultlist[x][y] = 1 # 그 위치의 빈칸에 벽 세우기

    for i in range(n):
        for j in range(m):
            if resultlist[i][j] == 2 and (i, j) not in visited: # 확산 체크용 지도에서 아직 방문하지 않은 모든 바이러스 칸에 대해
                dfs(resultlist, i, j, visited) # 바이러스 확산 체크 

    safe = sum(row.count(0) for row in resultlist) # 조합마다의 안전 영역 크기 저장
    max_safe = max(max_safe, safe) # 각 조합의 안전 영역 크기 중 최댓값

print(max_safe)