# 9465 스티커 (DP)

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]

    # n == 1 인 경우 둘 중 큰 값 하나만 선택
    if n == 1:
        print(max(sticker[0][0], sticker[1][0]))
        continue

    # dp[row][i]는 i열에서 row(0=위, 1=아래) 스티커를 선택했을 때 0~i열까지 얻을 수 있는 최대 점수
    dp = [[0] * n for _ in range(2)]

    # 첫 번째 열은 선택의 여지가 없으므로 그대로 가져옴
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]

    # 같은 행은 인접해서 선택이 불가능하므로 반드시 반대 행에서 옴
    dp[0][1] = sticker[0][1] + dp[1][0]
    dp[1][1] = sticker[1][1] + dp[0][0]

    # 세 번째 열부터 현재 스티커를 선택한다면, 이전 열(i-1) 또는 전전 열(i-2)에서 "반대 행"을 선택한 경우만 올 수 있음
    for i in range(2, n):
        dp[0][i] = sticker[0][i] + max(dp[1][i - 1], dp[1][i - 2])
        dp[1][i] = sticker[1][i] + max(dp[0][i - 1], dp[0][i - 2])

    # 마지막 열에서 최대값 출력
    print(max(dp[0][n - 1], dp[1][n - 1]))
