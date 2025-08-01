# 최단 경로
# p.262 실전 문제 9-3 전보

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수(n), 간선의 개수(m), 출발 도시 (c) 입력받기
n, m, c = map(int, input().split())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for _ in range(n + 1)]

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기 d
for _ in range(m):
    x, y, z = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[x].append((y, z))

# 다익스트라 알고리즘 정의
def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:  # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)

        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘 수행
dijkstra(c)

count = 0
time = []
for i in range(1, n + 1):
    if distance[i] == INF:
        continue
    else:  # 무한대 값이 아닐 때
        count += 1  # 도시 개수 카운트
        time.append(distance[i]) # 도시별 최소 거리 저장 

print(count-1, max(time)) # 출력