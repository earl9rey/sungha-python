# 구현
# p.115 실전 문제 4-3 게임 개발

n, m = map(int, input().split())
a, b, dir = map(int, input().split())

location = []

for i in range(n):
    loc = list(map(int, input().split()))
    location.append(loc)

visited = [(a, b)]

count = 0

while True:
    if count == 3:
        break
    if dir == 0:
        dir = 3
        if ((a, b-1) not in visited) and (location[a][b-1] == 0):
            b = b - 1
            visited.append((a, b))
            count = 0
        else:
            count += 1
    elif dir == 1:
        dir = 0
        if ((a-1, b) not in visited) and (location[a-1][b] == 0):
            a = a - 1
            visited.append((a, b))
            count = 0
        else:
            count += 1
    elif dir == 2:
        dir = 1
        if ((a, b+1) not in visited) and (location[a][b+1] == 0):
            b = b + 1
            visited.append((a, b))
            count = 0
        else:
            count += 1
    else:
        dir = 2
        if ((a+1, b) not in visited) and (location[a+1][b] == 0):
            a = a + 1
            visited.append((a, b))
            count = 0
        else:
            count += 1
    print(visited)

print(len(visited))
