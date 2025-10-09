# 쉬운 최단 거리 

from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[-1] * m for _ in range(n)]

# BFS 함수 정의
def bfs(graph, x, y):
    
    # 상하좌우 이동을 위한 방향 벡터
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))    # BFS 큐에 시작 좌표 추가
    visited[x][y] = 0       # 시작점 거리 = 0, 방문 처리

    # BFS 탐색 시작
    while queue:
        x, y = queue.popleft()   # 큐에서 현재 좌표 꺼내기

        # 상하좌우 이웃 탐색
        for i in range(4):
            nx = x + dx[i]      # 다음 x 좌표
            ny = y + dy[i]      # 다음 y 좌표

            # 지도 범위를 벗어나면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 갈 수 있는 땅(=1)이고, 아직 방문하지 않은 좌표라면
            if graph[nx][ny] == 1 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1  # 거리 갱신
                queue.append((nx, ny))               # 큐에 추가하여 BFS 계속


# 지도 전체 순회
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:       # 갈 수 없는 땅
            visited[i][j] = 0      # 거리 0으로 표시 (도달 불가)
        elif graph[i][j] == 2:     # 목표 위치
            bfs(graph, i, j)       # BFS 수행


for v in visited:
    print(*v)