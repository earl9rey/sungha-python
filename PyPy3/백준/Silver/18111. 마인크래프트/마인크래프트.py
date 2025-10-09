import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
ground = []

# 땅의 각 칸 높이 입력
for _ in range(n):
    height = list(map(int, input().split()))
    ground.append(height)

# 탐색할 높이 범위 (최솟값 ~ 최댓값)
start = min(min(row) for row in ground)
end = max(max(row) for row in ground)

lst = []  # (걸린 시간, 높이) 쌍을 저장

# 가능한 목표 높이 h를 하나씩 시도
for h in range(start, end+1):
    remove = 0  # 제거해야 할 블록 수
    build = 0   # 쌓아야 할 블록 수
    
    # 모든 좌표를 순회하면서 제거/쌓기 블록 개수 계산
    for i in range(n):
        for j in range(m):
            if ground[i][j] > h:
                # 현재 땅이 목표 높이보다 높음 → 블록 제거
                remove += ground[i][j] - h
            elif ground[i][j] < h:
                # 현재 땅이 목표 높이보다 낮음 → 블록 쌓기
                build += h - ground[i][j]
            else:
                continue  # 높이가 같으면 아무 작업 필요 없음
    
    # 제거해서 얻은 블록 + 초기 인벤토리 ≥ 쌓아야 할 블록 → 가능 여부 체크
    if remove + b >= build:
        # 총 시간 = 제거 블록 * 2초 + 쌓기 블록 * 1초
        time = remove * 2 + build
        lst.append([time, h])  # (시간, 높이) 기록

# 최소 시간을 우선으로, 시간이 같다면 더 높은 높이를 선택
t, h = min(lst, key=lambda x: (x[0], -x[1]))
print(t, h)