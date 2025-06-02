# DFS/BFS
# p.353 Q-21 인구 이동

from collections import deque

n, l, r = map(int, input().split())
population = [list(map(int, input().split())) for _ in range(n)]

def bfs(graph, x, y, federation, visited): # 연합을 찾고 연합에 속한 나라 좌표를 federation 리스트에 추가
    queue = deque()
    queue.append((x, y))           # 시작 위치를 큐에 넣음
    visited[x][y] = True           # 방문 처리
    federation.append((x, y))      # 현재 연합에 시작 위치 추가

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()     # 현재 위치 꺼냄

        for i in range(4):         # 상하좌우 네 방향 탐색
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:     # 지도 안에 있고 아직 방문하지 않은 위치일 경우
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:          # 인구 차이가 l 이상 r 이하이면 연합 가능
                    visited[nx][ny] = True      # 방문 처리
                    queue.append((nx, ny))      # 다음 탐색 대상으로 추가
                    federation.append((nx, ny)) # 연합 국가에 포함


visited = [[False] * n for _ in range(n)]  # 방문 여부 체크
day = 0  # 인구 이동이 발생한 날짜 수

while True:
    moved = False  # 이번 턴에 인구 이동이 있었는지 여부 표시

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:  # 아직 방문하지 않은 나라라면
                federation = []     # 새 연합 구성 리스트 초기화
                bfs(population, i, j, federation, visited) # 연합 국가 찾기 BFS 수행

                if len(federation) > 1:  # 연합 국가가 2개 이상이면 인구 이동 발생
                    moved = True         # 인구 이동 표시 True로 변경
                    total = sum(population[x][y] for x, y in federation) # 연합 내 전체 인구수 합산
                    avg = total // len(federation)      # 연합 내 각 나라가 가질 인구수 (평균)
                    
                    for x, y in federation: # 각 나라에 인구수 할당
                        population[x][y] = avg

    if not moved:    # 이번 턴에 인구 이동이 없으면 종료
        break

    day += 1        # 인구 이동 발생한 날 수 1 증가
    visited = [[False] * n for _ in range(n)]  # 방문 배열 초기화 (다음 날 탐색을 위해)

print(day)
