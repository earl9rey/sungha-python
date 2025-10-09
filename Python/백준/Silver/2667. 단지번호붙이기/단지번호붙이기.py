# 단지 번호 붙이기

from collections import deque

N = int(input())   # 지도의 크기 (N x N)

# 지도 정보를 2차원 리스트로 입력받음 (문자 → int 변환)
graph = [list(map(int, input())) for _ in range(N)]


# BFS 함수 정의
def bfs(graph, x, y):
    # 상하좌우 방향 이동 벡터
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))   # 시작 좌표 추가

    graph[x][y] = 0        # 현재 위치를 방문 처리 (0으로 바꿔 다시 방문하지 않도록)
    cnt = 1                # 단지에 포함된 집 개수 (시작점 포함)

    # BFS 탐색
    while queue:
        x, y = queue.popleft()

        # 상하좌우 이웃 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 지도 범위를 벗어나면 무시
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            # 집이 있는 곳(=1)이라면
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0         # 방문 처리
                queue.append((nx, ny))    # 큐에 추가
                cnt += 1                  # 단지 내 집 개수 증가
    return cnt   # 해당 단지의 집 개수 반환


# 모든 좌표를 돌며 집(=1)이 있으면 BFS 실행 → 단지 크기 계산
count = [bfs(graph, i, j) for i in range(N) for j in range(N) if graph[i][j] == 1]

count.sort()             # 단지 크기를 오름차순 정렬
print(len(count))        # 총 단지 수 출력

# 각 단지의 크기를 한 줄씩 출력
for i in range(len(count)):   
    print(count[i])
