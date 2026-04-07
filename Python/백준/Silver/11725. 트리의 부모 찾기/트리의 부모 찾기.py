import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

# 각 노드의 연결 정보를 저장할 그래프 (0번~n-1 사용)
graph = list([] for _ in range(n))

# parent[i] = i번 노드의 부모 노드 번호 저장
parent = [0] * n

# 방문 여부 체크 (0 = 미방문, 1 = 방문)
visited = [0] * n

# 트리는 n-1개의 간선 입력
for _ in range(n-1):
    a, b = map(int, input().split())
    # 입력은 1번 기반이므로 0번 기반으로 맞추기 위해 -1
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

# BFS 함수: 특정 시작 노드(v)에서부터 부모를 찾는다
def bfs(v, graph, visited):
    # queue에 시작 노드를 넣는다 (여기서는 v=1이라서 노드 1 넣음)
    que = deque([v])
    
    # 방문 처리 (v는 1-based라서 배열에서 v-1 처리)
    visited[v-1] = 1
    
    while que:                 # 큐가 빌 때까지 반복
        current = que.popleft()    # 현재 방문 중인 노드 (1-based)
        
        # current의 이웃 노드를 모두 확인
        for i in graph[current-1]:   # i는 0-based 노드 번호
            if visited[i] == 0:  # 아직 방문하지 않았다면
                parent[i] = current  # i의 부모는 current (여기서는 1-based)
                
                que.append(i+1)  # i는 0-based이므로 +1 해서 queue에 넣기
                visited[i] = 1   # 방문 처리

# 루트가 1번 노드이므로 1번부터 BFS 시작
bfs(1, graph, visited)

# 각 노드의 부모 출력 (문제 요구에 맞게 1번 노드는 제외)
for i, result in enumerate(parent):
    if i != 0:        # 0번 노드(실제 1번 노드)는 부모가 없으므로 건너뜀
        print(result)