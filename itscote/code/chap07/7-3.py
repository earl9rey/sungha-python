# 이진 탐색 
# p.201 실전 문제 7-3 떡볶이 떡 만들기

n, m = map(int, input().split())
height = list(map(int, input().split()))

def search(height, m, start, end):
    if start > end:
        return None
    mid = (start + end) //2     # mid - 자를 떡의 높이 설정
    sum = 0

    for h in height :           # 모든 떡에 대해서 
        if h > mid :
            sum += h - mid      # 자르고 남은 떡의 높이 총합 계산

    if sum == m :               # 원하는 양만큼 떡이 나왔을 때
        return mid
    elif sum < m :              # 원하는 양보다 떡이 부족할 때
        return search(height, m, start, mid-1)  # 자를 떡의 높이를 더 줄임 (end = mid-1)
    else:                        # 원하는 양보다 떡이 많을 때
        return search(height, m, mid+1, end)    # 자를 떡의 높이를 더 높임 (start = mid+1)
     

result = search(height, m, 0, max(height))
print(result)

