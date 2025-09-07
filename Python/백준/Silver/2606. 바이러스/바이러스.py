# 오답 - 1에 직접 연결된 컴퓨터만 감염  ------------------------------
    # n = int(input())
    # p = int(input())

    # computer = [[] for _ in range(n+1)]
    # virus = [0] * (n+1)

    # for _ in range(p) :
    #     a, b = map(int, input().split())
    #     computer[a].append(b)

    # virus[1] = 1
    # for i in range(n+1):
    #     if virus[i] == 1:
    #         for j in computer[i] :
    #             virus[j] = 1

    # count = 0
    # for i in virus :
    #     if i == 1 :
    #         count += 1

    # print(count - 1)
# --------------------------------------------------------

# DFS/BFS 문제
# DFS 이용

n = int(input())
p = int(input())

# 인접 리스트 초기화
computer = [[] for _ in range(n+1)]
virus = [0] * (n+1)

# 연결 관계 입력
for _ in range(p):
    a, b = map(int, input().split())
    computer[a].append(b)
    computer[b].append(a)  # 양방향 연결 추가

def dfs(node):
    virus[node] = 1
    for i in computer[node]:
        if virus[i] == 0:  # 아직 감염되지 않았다면
            dfs(i)

# 1번 컴퓨터에서 시작
dfs(1)

# 1번을 제외한 감염된 컴퓨터 수
print(sum(virus) - 1)