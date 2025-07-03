# DFS/BFS
# p.355 Q-22 블록 이동하기 (https://school.programmers.co.kr/learn/courses/30/lessons/60063)

from collections import deque

def get_next_pos(pos, board):
    next_pos = []
    pos = list(pos)  # 집합 -> 리스트
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

    # 상, 하, 좌, 우 이동
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        pos1_next_x = pos1_x + dx[i]
        pos1_next_y = pos1_y + dy[i]
        pos2_next_x = pos2_x + dx[i]
        pos2_next_y = pos2_y + dy[i]
        if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
            next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})

    # 가로로 놓인 경우 회전
    if pos1_x == pos2_x:
        for i in [-1, 1]:  # 위, 아래
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})

    # 세로로 놓인 경우 회전
    elif pos1_y == pos2_y:
        for i in [-1, 1]:  # 왼, 오
            if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})

    return next_pos

def solution(board):
    n = len(board)
    # 외곽에 벽 추가
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]

    # BFS
    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)}  # 시작 위치
    q.append((pos, 0))
    visited.append(pos)

    while q:
        pos, cost = q.popleft()
        if (n, n) in pos:
            return cost
        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)
    return 0
