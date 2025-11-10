# 16928 뱀과 사다리 게임

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
move = dict()

for _ in range(n+m):
    x, y  = map(int, input().split())
    move[x] = y

result = 100
visited = [0] * 101

def bfs():
    queue = deque()
    queue.append(1)
    visited[1] = 1

    while queue:
        current = queue.popleft()
        if current == 100 :
            print(visited[current] - 1) # 100 도착 시 횟수 출력 (시작 위치에 저장한 1 제외)
            break

        for n in range(1, 7):
            next = current + n

            if next in move: # 다음 위치에 사다리나 뱀이 있다면 이동
                next = move[next]
            if next > 100 or visited[next]: # 범위를 벗어나거나 이미 방문했으면 continue
                continue

            visited[next] =  visited[current] + 1
            queue.append(next)

bfs()