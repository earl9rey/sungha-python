# 7569 토마토

import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split()) 

# 3차원 배열 입력
ripen = []
for _ in range(h):
    box = [list(map(int, input().split())) for _ in range(n)]
    ripen.append(box)

# BFS용 방향 (좌, 우, 상, 하, 위, 아래)
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

queue = deque()

# 초기 익은 토마토 위치를 큐에 추가 (day = 0)
for z in range(h):
    for x in range(n):
        for y in range(m):
            if ripen[z][x][y] == 1:
                queue.append((z, x, y, 0))

result = 0

# BFS
while queue:
    z, x, y, day = queue.popleft()
    result = max(result, day) # 마지막으로 익은 토마토의 day
    
    for i in range(6):
        nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]
        if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
            if ripen[nz][nx][ny] == 0:
                ripen[nz][nx][ny] = 1
                queue.append((nz, nx, ny, day + 1))

# 모든 토마토 익었는지 확인
for z in range(h):
    for x in range(n):
        for y in range(m):
            if ripen[z][x][y] == 0:
                print(-1)
                exit()

print(result)
     