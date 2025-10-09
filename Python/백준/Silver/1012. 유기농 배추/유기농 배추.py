import sys
sys.setrecursionlimit(10**6) 

# 위 코드는 재귀의 한도를 풀어주는 함수이다.
# 만약 재귀를 사용해서 풀어야 하는 문제라면, 해당 코드는 선택이 아닌 필수이다.
# 파이썬의 기본 재귀 깊이 제한은 1000으로 매우 얕은 편이다.
# 따라서 재귀로 문제를 풀 경우 드물지 않게 이 제한에 걸리게 되는데, 문제는 코딩테스트 환경에서는 에러메세지를 볼 수 없다는 것이다. 
# 함정에 빠지지 않기 위해 재귀함수를 사용한다면 잊지말고 꼭 써주어야 한다.

t = int(input())  

def dfs(ground, x, y, visited) :
    # 상, 하, 좌, 우 이동 방향 (dx, dy)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 현재 위치 방문 처리
    visited.append((x, y))

    # 네 방향으로 탐색
    for i in range(4) :
        nx = x + dx[i]  # 다음 x좌표
        ny = y + dy[i]  # 다음 y좌표
    
        # 좌표가 유효한 범위 안에 있을 때만 진행
        if 0 <= nx < n and 0 <= ny < m:
            # 아직 방문하지 않았고, 배추가 있는 땅(=1)일 경우
            if (nx, ny) not in visited and ground[nx][ny] == 1:
                dfs(ground, nx, ny, visited)

# 테스트 케이스별 실행
for _ in range(t) :
    m, n, k = map(int, input().split())  
    # m: 가로(열 개수), n: 세로(행 개수), k: 배추 개수
    ground = [[0] * m for _ in range(n)]

    # 배추 위치 표시
    for _ in range(k) :
        x, y = map(int, input().split())
        ground[y][x] = 1  # (x, y) 좌표에 배추 심기

    visited = []  # 방문한 좌표 저장
    count = 0     # 지렁이 개수
    
    # 모든 좌표를 탐색
    for i in range(n) :       # 행 순회
        for j in range(m) :   # 열 순회
            # 배추가 있고, 아직 방문하지 않았다면
            if ground[i][j] == 1 and (i, j) not in visited:
                dfs(ground, i, j, visited)  # DFS 탐색 시작
                count += 1                  # 새로운 영역 → 지렁이 +1

    print(count)
