# 헌내기는 친구가 필요해

# 시간 초과 -------------------------------------------
    # import sys
    # sys.setrecursionlimit(10**6) # 런타임 에러 방지
    # input = sys.stdin.readline

    # n, m = map(int, input().split())
    # campus = [list(map(str, input())) for _ in range(n)]

    # visited = []  # 방문한 좌표를 저장하는 리스트
    # count = 0     # 친구(P) 발견 수

    # # DFS 탐색 함수
    # def dfs(campus, x, y, visited) :
    #     global count                 # 전역 변수 count 사용
    #     dx = [-1, 1, 0, 0]           # 상, 하 이동
    #     dy = [0, 0, -1, 1]           # 좌, 우 이동
        
    #     visited.append((x, y))       # 현재 위치 방문 처리

    #     # 상하좌우 탐색
    #     for i in range(4) :
    #         nx = x + dx[i]           # 다음 x좌표
    #         ny = y + dy[i]           # 다음 y좌표
        
    #         # 좌표가 캠퍼스 범위 안이고, 아직 방문하지 않았으며, 벽(X)이 아닌 경우
    #         if 0 <= nx < n and 0 <= ny < m:
    #             if (nx, ny) not in visited and campus[nx][ny] != 'X':
    #                 if campus[nx][ny] == 'P':  # 친구 발견 시
    #                     count += 1            # 카운트 증가
    #                 dfs(campus, nx, ny, visited)  # 재귀적으로 DFS 수행

    # # 출발점(I) 찾기
    # for i in range(len(campus)):
    #     for j in range(len(campus[i])):
    #         if campus[i][j] == 'I':
    #             x, y = i, j   # 출발점 좌표 저장


    # dfs(campus, x, y, visited)

    # if count == 0 :
    #     print('TT')
    # else:
    #     print(count)
# ------------------------------------------------------------

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]

visited = [[0] * m for _ in range(n)]
cnt = 0


def bfs(row, col):
    global cnt
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dq = deque()
    dq.append((row, col))
    visited[row][col] = 1
    while dq:
        r, c = dq.popleft()
        for i in range(4):
            nr = r + move[i][0]
            nc = c + move[i][1]
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            if graph[nr][nc] == 'X':
                continue
            if visited[nr][nc] == 1:
                continue
            visited[nr][nc] = 1
            dq.append((nr, nc))
            if graph[nr][nc] == 'P':
                cnt += 1

start = (0, 0)
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            start = (i, j)

bfs(start[0], start[1])

if cnt == 0:
    print("TT")
if cnt != 0:
    print(cnt)