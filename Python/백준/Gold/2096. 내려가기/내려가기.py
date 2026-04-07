# 2096 내려가기 (DP)

# 메모리 초과 -------------------------------------------------------------------------------------------

    # import sys
    # input = sys.stdin.readline

    # N = int(input())

    # # game[j][i] : j번째 줄의 i번째 숫자 (i = 0,1,2)
    # game = [list(map(int, input().split())) for _ in range(N)]

    # # N == 1이면 첫 줄에서 최댓값 / 최솟값이 답
    # if N == 1:
    #     print(max(game[0]), min(game[0]))
    #     sys.exit(0)

    # # dp[j][i] : j번째 줄의 i번째 숫자일 때 0 ~ j번째 줄까지 내려오며 얻을 수 있는 (최댓값, 최솟값)
    # dp = [[(0, 0) for _ in range(3)] for _ in range(N)]

    # # 첫 줄 초기화
    # for i in range(3):
    #     dp[0][i] = (game[0][i], game[0][i])

    # # DP - j번째 줄, i번째 칸에 도착하려면 바로 위 줄(j-1)에서 이동 가능한 칸에서만 올 수 있음
    # for j in range(1, N):
    #     for i in range(3):

    #         # i == 0 (왼쪽 칸) : 위 줄에서 0번 or 1번 칸에서만 내려올 수 있음
    #         if i == 0:
    #             max_prev = max(dp[j-1][0][0], dp[j-1][1][0])
    #             min_prev = min(dp[j-1][0][1], dp[j-1][1][1])

    #         # i == 1 (가운데 칸) : 위 줄의 세 칸(0,1,2) 모두에서 내려올 수 있음  
    #         elif i == 1:
    #             max_prev = max(dp[j-1][0][0], dp[j-1][1][0], dp[j-1][2][0])
    #             min_prev = min(dp[j-1][0][1], dp[j-1][1][1], dp[j-1][2][1])

    #         # i == 2 (오른쪽 칸) : 위 줄에서 1번 or 2번 칸에서만 내려올 수 있음
    #         elif i == 2:
    #             max_prev = max(dp[j-1][1][0], dp[j-1][2][0])
    #             min_prev = min(dp[j-1][1][1], dp[j-1][2][1])

    #         # 현재 칸(game[j][i])의 값 계산
    #         dp[j][i] = (game[j][i] + max_prev, game[j][i] + min_prev)


    # # 마지막 줄에서 결과 도출
    # MaxResult = max(dp[N-1][0][0], dp[N-1][1][0], dp[N-1][2][0])
    # MinResult = min(dp[N-1][0][1], dp[N-1][1][1], dp[N-1][2][1])

    # print(MaxResult, MinResult)

# -------------------------------------------------------------------------------------------

import sys
input = sys.stdin.readline

N = int(input())

# 첫 줄 입력
game = list(map(int, input().split()))

# dp[i] = i번째 칸까지 내려왔을 때의 (max, min)
dp = [
    (game[0], game[0]),
    (game[1], game[1]),
    (game[2], game[2])
]

# 두 번째 줄부터 처리
for _ in range(1, N):
    game = list(map(int, input().split()))

    dp0_max = game[0] + max(dp[0][0], dp[1][0])
    dp0_min = game[0] + min(dp[0][1], dp[1][1])

    dp1_max = game[1] + max(dp[0][0], dp[1][0], dp[2][0])
    dp1_min = game[1] + min(dp[0][1], dp[1][1], dp[2][1])

    dp2_max = game[2] + max(dp[1][0], dp[2][0])
    dp2_min = game[2] + min(dp[1][1], dp[2][1])

    # 현재 줄이 다음 반복의 이전 줄이 됨 (슬라이딩)
    dp = [
        (dp0_max, dp0_min),
        (dp1_max, dp1_min),
        (dp2_max, dp2_min)
    ]

# 마지막 줄 결과
MaxResult = max(dp[0][0], dp[1][0], dp[2][0])
MinResult = min(dp[0][1], dp[1][1], dp[2][1])

print(MaxResult, MinResult)