# 7576 토마토

import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split()) 

# 2차원 배열 입력
box = [list(map(int, input().split())) for _ in range(n)]

# BFS용 방향 (좌, 우, 상, 하, 위, 아래)
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]

queue = deque()

# 초기 익은 토마토 위치를 큐에 추가 (day = 0)
for x in range(n):
    for y in range(m):
        if box[x][y] == 1:
            queue.append((x, y, 0))

result = 0

# BFS
while queue:
    x, y, day = queue.popleft()
    result = max(result, day) # 마지막으로 익은 토마토의 day
    
    for i in range(6):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if box[nx][ny] == 0:
                box[nx][ny] = 1
                queue.append((nx, ny, day + 1))

# 모든 토마토 익었는지 확인
for x in range(n):
    for y in range(m):
        if box[x][y] == 0:
            print(-1)
            exit()

print(result)
     