# N과 M (12)
# 주어진 숫자들 중에서 중복을 제거한 뒤, 비내림차순(이전 숫자보다 같거나 큰) 순서로 길이 m짜리 수열 생성

n, m = map(int, input().split())
nums = [int(x) for x in input().split()]

# 입력된 숫자들 중복 제거 + 정렬
nums = sorted(list(set(nums)))
n = len(nums)

answer = []
seq = []

# num: 이번 단계에서 선택 가능한 최소 숫자(이전 숫자)
# depth: 현재 수열의 길이
def dfs(num, depth):
    # m개를 모두 채웠으면 출력
    if depth == m:
        print(" ".join(map(str, seq)))  # 리스트 → 문자열로 출력
        return

    # nums.index(num): num이 있는 위치 찾기
    # 이 위치부터 n까지 반복 → 비내림차순 유지됨
    for i in range(nums.index(num), n):

        seq.append(nums[i])         # 현재 숫자 추가
        dfs(nums[i], depth + 1)     # 다음 depth에서 nums[i] 이상만 선택
        seq.pop()                   # 끝나면 되돌리기 (백트래킹)

# DFS를 가장 작은 숫자부터 시작
dfs(nums[0], 0)
