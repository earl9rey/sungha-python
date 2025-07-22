# 이진 탐색 문제
# p.369 Q-29 공유기 설치 (지피띠니ㅠㅠ)

n, c = map(int, input().split()) 
house = [int(input()) for _ in range(n)]

house.sort()

# 공유기를 주어진 거리 이상 간격으로 설치할 수 있는지 확인하는 함수
def is_possible(distance):
    count = 1  # 첫 번째 집에는 무조건 설치
    last_pos = house[0]  # 가장 최근에 공유기를 설치한 집의 좌표

    # 두 번째 집부터 마지막 집까지 순회하며 공유기 설치 가능 여부 확인
    for i in range(1, n):
        # 현재 집이 마지막 설치 집으로부터 distance 이상 떨어져 있다면 설치
        if house[i] - last_pos >= distance:
            count += 1
            last_pos = house[i]  # 설치했으므로 최근 위치 갱신

    # 설치된 공유기 개수가 목표 개수 c 이상이면 True
    return count >= c


left = 1  # 가능한 최소 거리 (공유기 사이 간격)
right = house[-1] - house[0]  # 가능한 최대 거리 (가장 먼 두 집 사이 거리)
result = 0  # 최적의 최대 거리 저장용 변수

# 이진 탐색
while left <= right:
    mid = (left + right) // 2  # 현재 시도해볼 거리(중간값)

    if is_possible(mid):
        # 현재 거리로도 c개 이상 설치 가능 → 더 넓은 거리도 가능할지 탐색
        result = mid  # 일단 현재 거리 저장 (가능하니까 후보)
        left = mid + 1  # 거리를 더 넓혀보기 위해 오른쪽 탐색
    else:
        # 현재 거리로는 공유기 설치 불가 → 거리를 좁혀야 함
        right = mid - 1  # 왼쪽 탐색

print(result)
