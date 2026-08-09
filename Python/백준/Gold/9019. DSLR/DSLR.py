# 9019 DSLR

import sys
from collections import deque

T = int(input())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().rstrip().split()) 

    deq = deque()
    deq.append([A, '']) # 시작점

    visited = [False for i in range(10001)] 
    visited[A] = True

    # BFS 시작
    while deq:
        num, command = deq.popleft() # 현재 숫자와 명령어

        # 목표 숫자 B에 도달하면 결과 출력하고 탐색 종료
        if num == B:
            print(command)
            break

        # D 연산: 2배 (10000 넘으면 나머지)
        d = (num * 2) % 10000
        if not visited[d]:
            visited[d] = True
            deq.append([d, command + 'D'])

        # S 연산: 1 감소 (0이면 9999로)
        s = (num - 1) % 10000
        if not visited[s]:
            visited[s] = True
            deq.append([s, command + 'S'])

        # L 연산: 자릿수 왼쪽 회전
        l = (num % 1000) * 10 + num // 1000
        if not visited[l]:
            visited[l] = True
            deq.append([l, command + 'L'])

        # R 연산: 자릿수 오른쪽 회전
        r = (num // 10) + (num % 10) * 1000
        if not visited[r]:
            visited[r] = True
            deq.append([r, command + 'R'])
