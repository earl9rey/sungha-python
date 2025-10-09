# 연결 요소의 개수

import sys
sys.setrecursionlimit(10**6) # 재귀 깊이 제한 조정
input = sys.stdin.readline


n, m = map(int, input().split())

# graph = [[]] * (n+1) --> 같은 리스트 객체를 얕은 복사 (모든 인덱스가 전부 동일한 리스트 객체 참조)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n+1)
connected = 0

# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


for i in range(1, n+1) :
    if not visited[i]:   # 아직 방문하지 않은 정점에서만 DFS 시작
        dfs(graph, i, visited)
        connected += 1 # 한 번 순환 시 연결 요소 개수 + 1

print(connected)
