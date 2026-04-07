# 1504 특정한 최단 경로

import sys
import heapq
input = sys.stdin.readline

# N: 정점 개수
# E: 간선 개수
N, E = map(int, input().split())

# 그래프를 인접 리스트 형태로 저장
# graph[i] = [(연결된 정점, 거리), ...]
graph = [[] for _ in range(N+1)]

# 간선 정보 입력
for _ in range(E):
    a, b, c = map(int, input().split())
    
    # a → b 거리 c
    graph[a].append((b, c))
    
    # 문제에서 "양방향 그래프"이므로
    # b → a도 같은 거리로 연결
    graph[b].append((a, c))

# 반드시 거쳐야 하는 두 정점
v1, v2 = map(int, input().split())


# 다익스트라 알고리즘
# start 정점에서 모든 정점까지의 최단 거리 계산
def dijkstra(start):
    
    # dist[i] = start → i 까지의 현재까지 알려진 최단 거리
    dist = [float('inf')] * (N+1)
    
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


# 다익스트라 3번 실행
# 이유: 필요한 거리들을 계산하기 위해
# 1 → 모든 정점
# v1 → 모든 정점
# v2 → 모든 정점

dist1 = dijkstra(1)
distv1 = dijkstra(v1)
distv2 = dijkstra(v2)


# 경로 1
# 1 → v1 → v2 → N
# 각 구간의 최단거리 합
path1 = dist1[v1] + distv1[v2] + distv2[N]


# 경로 2
# 1 → v2 → v1 → N
path2 = dist1[v2] + distv2[v1] + distv1[N]


# 두 경로 중 더 짧은 것 선택
answer = min(path1, path2)


# 만약 경로가 존재하지 않으면
# 거리값이 여전히 무한대(inf)이므로 -1 출력
if answer == float('inf'):
    print(-1)
else:
    print(answer)