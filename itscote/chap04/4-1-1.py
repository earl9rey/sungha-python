# 구현
# p.110 예제 4-1 상하좌우

size = int(input())
move = list(map(str, input().split()))

row = 1
col = 1

for i in range(len(move)) :
    if move[i] == 'L' :
        if col == 1 :
            continue
        col -= 1
    elif move[i] == 'R' :
        if col == size :
            continue
        col += 1
    elif move[i] == 'U' :
        if row == 1 :
            continue
        row -= 1
    else :
        if row == size :
            continue
        row += 1

print(row, col)

