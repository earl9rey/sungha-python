# 숨바꼭질 (구글링)

from collections import deque

n, k = map(int, input().split())   # 시작 위치 n, 목표 위치 k 입력
MAX = 100000                       # 좌표의 최댓값 (문제 조건)
visited = [0] * (MAX+1)            # 각 위치까지 걸린 시간을 저장하는 배열

def bfs(n):
    q = deque([n])                 # 큐 생성 후 시작점 n 삽입

    while q:                       # 큐가 빌 때까지 반복
        x = q.popleft()            # 현재 위치 꺼내기

        if x == k:                 # 목표 위치에 도달하면
            return visited[x]       # 해당 위치까지 걸린 시간 반환

        # 이동할 수 있는 3가지 경우 탐색
        for nx in (x-1, x+1, x*2):
            # 범위 안에 있고, 아직 방문하지 않은 위치라면
            if 0 <= nx <= MAX and visited[nx] == 0:
                visited[nx] = visited[x] + 1   # 이동 시간 갱신 (현재까지 + 1)
                q.append(nx)                   # 다음 탐색을 위해 큐에 추가

print(bfs(n))   # 시작 위치 n에서 목표 k까지의 최소 시간 출력

