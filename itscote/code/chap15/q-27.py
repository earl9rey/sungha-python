# 이진 탐색 문제
# p.367 Q-27 정렬된 배열에서 특정 수의 개수 구하기

n, x = map(int, input().split())
arr = list(map(int, input().split()))

# 이진 탐색으로 x의 첫번째 위치 찾기
def first(arr, target):
    start = 0
    end = len(arr) - 1

    result = -1  # 찾지 못하면 -1 유지

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            result = mid        # 일단 현재 위치를 저장하고
            end = mid - 1       # 더 왼쪽에 있는지 확인하러 감 (왼쪽으로 탐색)
        elif arr[mid] > target:
            end = mid - 1       # 너무 크면 왼쪽으로 이동
        else:
            start = mid + 1     # 너무 작으면 오른쪽으로 이동
    return result  # x가 처음 등장한 인덱스 또는 -1

# 이진 탐색으로 x의 마지막 위치 찾기
def last(arr, target):
    start, end = 0, len(arr) - 1
    result = -1  # 찾지 못하면 -1 유지
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            result = mid        # 일단 현재 위치 저장하고
            start = mid + 1     # 더 오른쪽에 같은 값이 있는지 확인하러 감 (오른쪽 탐색)
        elif arr[mid] > target:
            end = mid - 1       # 너무 큰 값 → 왼쪽으로
        else:
            start = mid + 1     # 너무 작은 값 → 오른쪽으로
    return result  # x가 마지막으로 등장한 인덱스 또는 -1

# 두 함수로 x의 시작/끝 위치를 찾음
first = first(arr, x)
last = last(arr, x)

# x가 배열에 존재하지 않으면 -1 출력
if first == -1 or last == -1:
    print(-1)
else:
    # 등장 횟수 = 마지막 인덱스 - 첫 번째 인덱스 + 1
    print(last - first + 1)