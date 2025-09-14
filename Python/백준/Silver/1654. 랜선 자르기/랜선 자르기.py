# 랜선 자르기 (이진 탐색)

import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lan = [int(input()) for _ in range(K)]

start = 1
end = max(lan)

while start <= end:
    mid = (start + end) // 2  # 중간 길이(자를 길이) 후보
    lines = 0  # 잘라서 얻을 수 있는 랜선 개수
    
    # 모든 랜선을 mid 길이로 잘랐을 때 얻을 수 있는 총 개수 계산
    for i in lan:
        lines += i // mid
        
    # 얻은 랜선이 N개 이상이면 → 더 긴 길이도 가능
    if lines >= N: 
        start = mid + 1
    # 얻은 랜선이 N개보다 적으면 → 길이를 줄여야 함
    else:
        end = mid - 1

print(end)
