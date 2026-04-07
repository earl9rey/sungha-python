# 1916 최소비용 구하기 (다익스트라)

import sys
import heapq
input = sys.stdin.readline

INF = 10**8  

N = int(input())  # 도시(노드) 개수
M = int(input())  # 버스(간선) 개수

# graph[u] = [(v, cost), ...] 
# u에서 v로 가는 버스 비용 목록
graph = [[] for _ in range(N + 1)]

# 간선 입력 (방향 그래프)
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 출발 도시, 도착 도시
start, end = map(int, input().split())

# dist[x] = start에서 x까지의 "현재까지 알고 있는" 최소 비용
dist = [INF] * (N + 1)
dist[start] = 0 


# 우선순위 큐(최소 힙)
# (현재까지의 비용, 도시) 형태로 저장 → 비용이 가장 작은 것부터 꺼내짐
pq = [(0, start)]

while pq:
    cost, now = heapq.heappop(pq)  # 지금까지 비용이 가장 작은 도시를 꺼냄

    # 이미 더 좋은(더 작은) 비용으로 now에 도달한 적이 있으면 스킵
    if dist[now] < cost:
        continue

    # now에서 갈 수 있는 모든 다음 도시(nxt) 확인
    for nxt, nxt_cost in graph[now]:
        new_cost = cost + nxt_cost

        # 더 싼 경로를 찾으면 dist 갱신하고 큐에 넣음
        if new_cost < dist[nxt]:
            dist[nxt] = new_cost
            heapq.heappush(pq, (new_cost, nxt))

# 도착 도시까지의 최소 비용 출력
print(dist[end])
