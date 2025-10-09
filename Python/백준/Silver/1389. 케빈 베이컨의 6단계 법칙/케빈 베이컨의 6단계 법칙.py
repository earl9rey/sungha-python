# 케빈 베이컨의 6단계 법칙
import sys
from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = 1
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[v] + 1

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m) :
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 각 노드가 방문된 정보를 리스트 자료형으로 표현 (1차원 리스트)
result = []

# 모든 친구 탐색 
for i in range(1, n+1):
    visited = [0] * (n+1)

    bfs(graph, i, visited)
    result.append(sum(visited)) # 각 친구의 베이컨 수를 리스트에 저장

print(result.index(min(result))+1) # 원소의 값이 가장 작을 때의 인덱스 +1 출력

    

