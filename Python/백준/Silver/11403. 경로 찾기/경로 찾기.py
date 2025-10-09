# 경로 찾기

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 결과를 저장할 n x n 행렬
# result[i][j] == 1이면 i에서 j로 가는 경로 존재
result = [[0] * n for _ in range(n)]

# 모든 정점을 시작점으로 BFS 실행
for i in range(n):  # i = 시작 노드
    visited = [0] * n          # i에서 도달 가능한 노드를 기록할 배열
                               # visited[j] == 1이면 i에서 j로 도달 가능
    q = deque([i])             # BFS 큐 초기화, 시작 노드 넣기

    # BFS 수행
    while q:                   # 큐가 빌 때까지 반복
        v = q.popleft()        # 큐에서 현재 노드 꺼내기
        for nxt in range(n):   # 현재 노드 v와 연결된 모든 노드 탐색
            # graph[v][nxt] == 1이면 v -> nxt 간선 존재
            # visited[nxt] == 0이면 아직 방문하지 않은 노드
            if graph[v][nxt] and not visited[nxt]:
                visited[nxt] = 1  # i에서 nxt로 도달 가능 표시
                q.append(nxt)     # nxt를 큐에 넣어 더 탐색

    # i에서 시작한 BFS 결과를 결과 행렬에 저장
    result[i] = visited

# 결과 행렬 출력
for row in result:
    print(*row)  # 공백으로 구분하여 한 행씩 출력
