# 최단 경로
# p.259 실전 문제 9-2 미래 도시

INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기
n, m = map(int, input().split())

# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아 초기화
for _ in range(m):
    # a에서 b로 가는 비용이 c라고 설정
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐 갈 노드 X와 최종 목적지 노드 K를 입력받기
x, k = map(int, input().split())

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):        # 거쳐가는 노드
    for a in range(1, n + 1):    # 출발 노드
        for b in range(1, n + 1):  # 도착 노드
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 거리 합 계산: 1에서 k까지 + k에서 x까지
distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print(-1)
else:
    print(distance)
