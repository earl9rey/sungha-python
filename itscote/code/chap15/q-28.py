# 이진 탐색 문제
# p.368 Q-28 고정점 찾기

n = int(input())
arr = list(map(int, input().split()))

def search(arr):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == mid:
            return mid  # 고정점 발견
        elif arr[mid] > mid:
            end = mid - 1  # 왼쪽에 있을 수 있음
        else:
            start = mid + 1  # 오른쪽에 있을 수 있음

    return -1  # 고정점 없음

print(search(arr))