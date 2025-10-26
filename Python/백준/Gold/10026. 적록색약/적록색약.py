#10026 적록색약

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
img = [list(input().strip()) for _ in range(n)]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            # 배열 범위 내, 색깔 같고, 방문 안한 경우
            if 0 <= nx < n and 0 <= ny < n and img[x][y] == img[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1  # 방문 처리
                q.append((nx, ny))

r1, r2 = 0, 0

# 적록색약이 아닌 사람이 볼 때의 그룹 개수
visited = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            r1 += 1

# 적록색맹이 볼 때의 그룹 개수를 새기 위하여 초록색을 빨간색으로 변경
for i in range(n):
    for j in range(n):
        if img[i][j] == 'G':
            img[i][j] = 'R'

# 적록색맹인이 볼 때의 그룹 개수
visited = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            r2 += 1

print(r1, r2)