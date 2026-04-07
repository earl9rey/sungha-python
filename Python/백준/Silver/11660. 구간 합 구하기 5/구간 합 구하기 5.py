# 11660 구간 합 구하기 5

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
num = [list(map(int, input().split())) for _ in range(N)]

# 완전 탐색 (시간 초과) -----------------------------
  # for _ in range(M):
  #     x1, y1, x2, y2 = map(int, input().split())

  #     total = 0

  #     for i in range(x1 - 1, x2):
  #         for j in range(y1 - 1, y2):
  #             total += num[i][j]

  #     print(total)
# -----------------------------------------------

dp = [[0] * (N+1) for _ in range (N+1)]

# 누적합 DP 계산 (Bottom-Up)
for i in range (1, N+1) :
    for j in range (1, N+1) :
        # 위 + 왼쪽 누적 − 중복 + 현재값
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + num[i-1][j-1]

# 구간 계산 
for _ in range (M) :
    x1, y1, x2, y2 = map(int, input().split())

    # 큰 사각형 − 필요 없는 위쪽 − 필요 없는 왼쪽 + 겹친 부분 보정
    result = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]

    print(result)
