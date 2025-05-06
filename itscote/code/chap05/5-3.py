# DFS/BFS
# p.149 실전 문제 5-3 음료수 얼려 먹기

n, m = map(int, input().split())
frame = [list(map(int, input())) for _ in range(n)]

visited=[]
count = 0

def dfs(frame, x, y, visited) :
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visited.append((x, y))

    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
    
        if 0 <= nx < n and 0 <= ny < m:
            if (nx, ny) not in visited and frame[nx][ny] == 0:
                dfs(frame, nx, ny, visited)
    
    
for i in range(n) :
    for j in range(m) :
        if frame[i][j] == 0 and (i, j) not in visited:
            dfs(frame, i, j, visited) 
            count += 1         

print(count)
         