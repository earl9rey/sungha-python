# 13549 숨바꼭질 3

from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

MAX = 100000
dist = [-1] * (MAX + 1)

dq = deque()
dq.append(N)
dist[N] = 0

while dq:
    x = dq.popleft()

    # 동생 위치 도착하면 바로 종료
    if x == K:
        print(dist[x])
        break

    # 순간이동 (비용 0)
    nx = x * 2
    if 0 <= nx <= MAX and dist[nx] == -1:
        dist[nx] = dist[x]
        dq.appendleft(nx)   # 비용 0 → 앞에 삽입

    # 걷기 (비용 1): x - 1
    nx = x - 1
    if 0 <= nx <= MAX and dist[nx] == -1:
        dist[nx] = dist[x] + 1
        dq.append(nx)       # 비용 1 → 뒤에 삽입

    # 걷기 (비용 1): x + 1
    nx = x + 1
    if 0 <= nx <= MAX and dist[nx] == -1:
        dist[nx] = dist[x] + 1
        dq.append(nx)       # 비용 1 → 뒤에 삽입