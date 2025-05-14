# DFS/BFS
# p.339 Q-15 특정 거리의 도시 찾기

from collections import deque

n, m, k, x= map(int, input().split())
road = [list(map(int, input().split())) for _ in range(m)]

# road 정보를 이용하여 연결 리스트 생성
graph = [[] for _ in range(n+1)] 

for i in road:
    start = i[0]
    graph[start].append(i[1])
 
print(graph)
print("============================")


# 각 도시에 대한 거리를 저장할 리스트 (도시 번호 = 인덱스)
distance = [[] for _ in range(n)]

# 최단 거리 구하는 문제에서는 bfs(너비우선탐색) 먼저 사용해보기
def bfs(graph, start, distance):
    queue = deque([start])
    distance[start] = 0

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if distance[i] == -1: # 아직 방문하지 않은 도시에 대해
                queue.append(i) # 방문 처리
                distance[i] = distance[v] + 1 # 이전 도시의 거리에 +1

distance = [-1] * (n+1)
bfs(graph, x, distance)

find = False
for i in range(n+1):
    if distance[i] == k : # 거리가 k인
        print(i) # 도시 번호 찾기
        find = True    # 찾았으면 True
        
if find == False:       # 못 찾았으면 -1 출력
    print(-1)

