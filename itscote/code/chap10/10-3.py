# 그래프 이론
# p.300 실전 문제 10-3 도시 분할 계획

# 특정 원소가 속한 집합을 찾기 (Find)
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])  # 경로 압축
    return parent[x]

# 두 원소가 속한 집합을 합치기 (Union)
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수(V), 간선의 개수(E) 입력받기
n, m = map(int, input().split())
parent = [0] * (n + 1)  # 부모 테이블 초기화

# 모든 간선을 담을 리스트와 최종 비용 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, n + 1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력받기
for _ in range(m):
    a, b, cost = map(int, input().split())
    # (비용, 노드1, 노드2) 형태로 저장 (정렬 기준이 비용이 되도록)
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()
maxcost = 0

# 간선을 하나씩 확인
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        maxcost = cost # 제일 마지막에 저장된 비용 (비용순으로 정렬했으므로 최대 비용)

print(result-maxcost)