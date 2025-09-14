# 나무 자르기

# 시간 초과 -----------------------------------------------------------------------

    # import sys
    # input = sys.stdin.readline

    # n, m = map(int, input().split())
    # tree = list(map(int, input().split()))

    # # 이진 탐색 범위 설정
    # start = 1          # 최소 자를 높이
    # end = max(tree)    # 최대 자를 높이 = 가장 긴 나무

    # # 이진 탐색으로 최적의 절단 높이 찾기
    # while start <= end:
    #     mid = (start + end) // 2  # 현재 자를 높이 후보
    #     length = 0                # 잘라서 얻을 수 있는 나무 길이 합계
        
    #     # 모든 나무에 대해 mid 높이로 잘랐을 때 얻는 나무 길이 계산
    #     for i in tree:
    #         if i >= mid:           # 나무가 mid 이상이면
    #             length += (i - mid)  # 잘라서 얻는 길이를 합산
    #         else:                  # 나무가 mid 이하이면
    #             length += 0         # 얻는 길이 없음
        
    #     # 잘라서 얻은 길이가 필요한 길이보다 크거나 같으면
    #     if length >= m:
    #         start = mid + 1   # 더 높게 잘라도 되므로 start 증가
    #     else:
    #         end = mid - 1     # 너무 길게 잘라서 모자라면 end 감소

    # # end가 최적의 절단 높이 (최대)
    # print(end)

# ------------------------------------------------------------------------------------

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))

# 이진 탐색 범위 설정
start = 1          # 최소 자를 높이
end = max(tree)    # 최대 자를 높이 = 가장 긴 나무

# 이진 탐색으로 최적의 절단 높이 찾기
while start <= end:
    mid = (start + end) // 2  # 현재 자를 높이 후보
    length = 0                # 잘라서 얻을 수 있는 나무 길이 합계
    
    # 모든 나무에 대해 mid 높이로 잘랐을 때 얻는 나무 길이 계산
    for i in tree:
        if i > mid:           # 나무가 mid 이상이면
            length += (i - mid)  # 잘라서 얻는 길이를 합산

        if length > m : # 절단된 나무를 추가하는 도중 이미 m을 넘어버린 경우 중단 --> 시간 초과 X
            break
    
    # 잘라서 얻은 길이가 필요한 길이보다 크거나 같으면
    if length >= m:
        start = mid + 1   # 더 높게 잘라도 되므로 start 증가
    else:
        end = mid - 1     # 너무 길게 잘라서 모자라면 end 감소

# end가 최적의 절단 높이 (최대)
print(end)