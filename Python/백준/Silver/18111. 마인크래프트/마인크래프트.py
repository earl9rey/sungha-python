# 마인크래프트

# 시간 초과 (pypy3로 하면 정답 ㅠㅠ) -----------------------------------------------------
    # import sys
    # input = sys.stdin.readline

    # n, m, b = map(int, input().split())
    # ground = []

    # # 땅의 각 칸 높이 입력
    # for _ in range(n):
    #     height = list(map(int, input().split()))
    #     ground.append(height)

    # # 탐색할 높이 범위 (최솟값 ~ 최댓값)
    # start = min(min(row) for row in ground)
    # end = max(max(row) for row in ground)

    # lst = []  # (걸린 시간, 높이) 쌍을 저장

    # # 가능한 목표 높이 h를 하나씩 시도
    # for h in range(start, end+1):
    #     remove = 0  # 제거해야 할 블록 수
    #     build = 0   # 쌓아야 할 블록 수
        
    #     # 모든 좌표를 순회하면서 제거/쌓기 블록 개수 계산
    #     for i in range(n):
    #         for j in range(m):
    #             if ground[i][j] > h:
    #                 # 현재 땅이 목표 높이보다 높음 → 블록 제거
    #                 remove += ground[i][j] - h
    #             elif ground[i][j] < h:
    #                 # 현재 땅이 목표 높이보다 낮음 → 블록 쌓기
    #                 build += h - ground[i][j]
    #             else:
    #                 continue  # 높이가 같으면 아무 작업 필요 없음
        
    #     # 제거해서 얻은 블록 + 초기 인벤토리 ≥ 쌓아야 할 블록 → 가능 여부 체크
    #     if remove + b >= build:
    #         # 총 시간 = 제거 블록 * 2초 + 쌓기 블록 * 1초
    #         time = remove * 2 + build
    #         lst.append([time, h])  # (시간, 높이) 기록

    # # 최소 시간을 우선으로, 시간이 같다면 더 높은 높이를 선택
    # t, h = min(lst, key=lambda x: (x[0], -x[1]))
    # print(t, h)

# --------------------------------------------------------------------

import sys 
input = sys.stdin.readline

# 모든 땅의 높이를 h로 만드는데 걸리는 시간을 구하는 함수 
def get_time(h):
    add_num = 0   # 삽입할 블록의 개수 
    erase_num = 0 # 제거할 블록의 개수 

    # 0부터 256까지 각 높이의 경우를 모두 탐색
    for i in range(257):
        # 높이의 개수와 h와의 차를 구해줌 
        n, tmp = nums[i], i - h 
        # 개수가 0이라면 넘어감 
        if n == 0: continue 
        # 높이의 차가 음수일 경우 삽입할 블록의 개수 구해줌 
        if tmp < 0:
            add_num += (-tmp) * n 
        # 높이의 차가 양수일 경우 제거할 블록의 개수 구해줌 
        else:
            erase_num += tmp * n 
    
    # 만약 인벤토리에서 사용할 수 있는 블록이 있을 경우 
    if (erase_num + b) - add_num >= 0:
        # 시간을 구해줌 
        time = erase_num * 2 + add_num 
        return time 
    # 사용할 수 있는 블록이 없을 경우 
    else:
        return 1e9 + 1
            
n, m, b = map(int,input().split())

# 땅 높이 종류의 각 개수를 구해줌 
nums = [0] * 257 
for i in range(n):
    for j in list(map(int,input().split())):
        nums[j] += 1 

# 최소 시간과 그 때의 높이를 저장할 변수 
ans = 1e9 
height = 0

# 0부터 256까지 모든 땅을 각 높이로 만드는 시간을 구해줌 
for h in range(257):
    # 시간을 계산 
    time = get_time(h)
    # 최소값과 그 때의 땅 높이를 구해줌  
    if time <= ans:
        ans = time 
        height = h 

print(ans, height)