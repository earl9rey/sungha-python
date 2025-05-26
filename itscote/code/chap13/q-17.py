# DFS/BFS
# p.344 Q-17 경쟁적 전염
from collections import deque

n, k = map(int, input().split())
test = [list(map(int, input().split())) for _ in range(n)]
s, sx, sy = map(int, input().split())


def bfs(virus, test, s) : 
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque(virus)
    
    while queue: # 바이러스 리스트 큐 빌 때까지 반복 (모든 바이러스 번호에 대해 순차적으로 검사)
        knum, time, x, y = queue.popleft() # 바이러스 리스트에서 값 추출

        if time == s: # 카운트한 시간이 s와 같아지면 break
            break

        for i in range(4) : #상하좌우로 움직이면서
            nx = x + dx[i]
            ny = y + dy[i]
    
            if (0 <= nx < n and 0 <= ny < n) :
                if test[nx][ny] == 0 : # 이동할 칸이 비어있으면
                    test[nx][ny] = knum # 그 칸에 바이러스 번호 k 넣고
                    time += 1 # 시간 카운트 증가
                    queue.append((knum, time, nx, ny)) # 방문했으니까 큐에 넣기


virus = []
for i in range(n) :
    for j in range(n) :
        if test[i][j] != 0 :
            virus.append((test[i][j], 0, i, j)) # 바이러스 리스트 = [(k번호, 시간, 시작위치 x, 시작 위치 y), ...]
virus.sort() # 바이러스 번호가 작은 것부터 나열

bfs(virus, test, s)
print(test[sx - 1][sy - 1])

# 처음에는 virus[test[i][j]] = (i, j) 
# 인덱스 번호가 바이러스의 종류, 그 인덱스의 값이 바이러스 위치 (x, y)가 되도록 바이러스 리스트를 생성
# 바이러스의 종류를 인덱스로 해서 해당 바이러스의 위치를 기록하려는 시도인데, 이건 바이러스가 하나씩만 존재할 경우에만 유효
# 바이러스 1번이 여러 곳에 퍼져 있다면 virus[1] = (i, j) 이렇게 저장하면, 가장 마지막에 나온 (i, j)만 저장되고 이전 위치들은 덮어씌워져서 사라짐
# virus를 리스트로 두되, 바이러스 종류별로 좌표 여러 개 저장하는 방식으로 전환