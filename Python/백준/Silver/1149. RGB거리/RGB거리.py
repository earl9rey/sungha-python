# 1149 RGB 거리

import sys
input = sys.stdin.readline

N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*3 for _ in range(N)]
dp[0] = cost[0][:] # 0번째 집은 처음과 동일

for i in range(1, N):
    dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])  # R - R(0)를 선택한다면 이전 집은 G(1) 또는 B(2) 중 최소 비용을 골라야 함
    dp[i][1] = cost[i][1] + min(dp[i-1][0], dp[i-1][2])  # G - G(1)를 선택한다면 이전 집은 R(0) 또는 B(2) 중 최소 비용을 골라야 함
    dp[i][2] = cost[i][2] + min(dp[i-1][0], dp[i-1][1])  # B - B(2)를 선택한다면 이전 집은 R(0) 또는 G(1) 중 최소 비용을 골라야 함

print(min(dp[N-1]))
