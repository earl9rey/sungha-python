from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

# 각 노드가 연결된 정보를 리스트 자료형으로 표현 2차원 리스트）
for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 모든 노드의 인접 리스트를 정렬 (번호 작은 것부터 방문)
for g in graph:
    g.sort()

# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


# 각 노드가 방문된 정보를 리스트 자료형으로 표현 1차원 리스트）
visited = [False] * (n+1)
dfs(graph, v, visited)
print()


from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 방문된 정보를 리스트 자료형으로 표현 (1차원 리스트)
visited = [False] * (n+1)
bfs(graph, v, visited)