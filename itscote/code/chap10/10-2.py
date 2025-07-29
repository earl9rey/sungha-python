# 그래프 이론
# p.298 실전 문제 10-2 팀 결성

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면 루트를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])  # 경로 압축
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
n, m = map(int, input().split())
parent = [0] * (n + 1) # 부모 테이블 초기화

# 부모 테이블에서 부모를 자기 자신으로 초기화
for i in range(1, n + 1):
    parent[i] = i

# union 연산을 각각 수행
for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0 : # union 연산일 때
        union_parent(parent, a, b)
    else : # 같은 팀 여부 확인일 때 
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')