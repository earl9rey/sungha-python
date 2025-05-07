# 구현 문제
# p.335 Q-14 외벽 점검

from itertools import combinations

# 리스트를 회전시켜 모든 시작 위치에 대해 순열을 만듦
def rotate_list(arr):
    return [arr[i:] + arr[:i] for i in range(len(arr))]

# 리스트 길이(length)를 n개로 나누기 위한 컷 포인트(자르는 인덱스) 생성
# n개로 자르기 위해선 (n - 1)개의 컷 포인트가 필요
def split_indices(length, n):
    if n <= 1:
        return [()]  # 자를 필요 없을 경우 빈 튜플 하나 리턴
    return combinations(range(1, length), n - 1)

# 주어진 리스트를 n개의 구간으로 나누고, 각 구간의 합을 계산해 반환
def split_and_sum(arr, n):
    all_results = []
    for rotation in rotate_list(arr):  # 리스트 회전한 모든 경우에 대해
        for cut_points in split_indices(len(rotation), n):  # 위치 조합 가능한 만큼 자르기
            parts = []
            prev = 0
            for idx in cut_points:
                parts.append(rotation[prev:idx])  # 자른 부분 추가
                prev = idx
            parts.append(rotation[prev:])  # 마지막 덩어리 추가

            # 각 조각의 합을 구하고, 내림차순으로 정렬
            part_sums = [sum(part) for part in parts]
            part_sums.sort(reverse=True)

            # 결과 저장
            all_results.append({
                "rotation": rotation,
                "parts": parts,
                "sums": part_sums
            })
    return all_results


def solution(n, weak, dist):
    distance = []

    # weak 지점들 사이의 거리 계산
    for i in range(len(weak)):
        if i == len(weak)-1:
            # 마지막과 첫 번째 지점 사이 거리 (원형)
            distance.append(n-1 - weak[i] + weak[0])
        else:
            distance.append(weak[i+1] - weak[i])

    print("distance:", distance)  # 디버깅용 출력

    # dist의 길이만큼 시도 (최대 투입 가능한 친구 수)
    for i in range(1, len(dist) + 1):
        result = split_and_sum(distance, i)  # 거리 리스트를 i개의 조각으로 나눔
        for r in result:
            # 가장 긴 거리 덩어리 하나라도 i번째 친구가 커버할 수 있다면 성공
            if r['sums'][0] <= dist[i - 1]:
                return i  # 필요한 친구 수 i 반환

    return -1  # 모든 경우에도 불가능하면 -1 반환
