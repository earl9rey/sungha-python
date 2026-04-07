# 1753 최단경로

import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

# 그래프를 인접 리스트 형태로 저장
# graph[i] = [(연결된 정점, 거리), ...]
graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())

    # u → v 가중치 w
    graph[u].append((v, w))


# 다익스트라 알고리즘
# start 정점에서 모든 정점까지의 최단 거리 계산
def dijkstra(start):
    
    # dist[i] = start → i 까지의 현재까지 알려진 최단 거리
    dist = [float('inf')] * (V+1)
    
    # 시작점 거리 = 0
    dist[start] = 0
    
    # 우선순위 큐 (heap)
    # (거리, 정점) 형태로 저장
    pq = []
    heapq.heappush(pq, (0, start))
    
    # 큐가 빌 때까지 반복
    while pq:
        cost, node = heapq.heappop(pq)
        
        # 이미 더 짧은 거리로 방문된 적 있으면 무시
        if dist[node] < cost:
            continue
        
        # 현재 정점과 연결된 모든 정점 확인
        for next_node, next_cost in graph[node]:
            
            # 현재 정점을 거쳐서 가는 거리 계산
            new_cost = cost + next_cost
            
            # 기존 거리보다 짧으면 갱신
            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))
    
    # start에서 모든 정점까지의 최단 거리 반환
    return dist


dist = dijkstra(K)

for i in range(1, V+1):
    if dist[i] == float('inf'):
        print("INF")
    else:
        print(dist[i])