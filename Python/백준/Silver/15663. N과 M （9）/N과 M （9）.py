# N과 M (9)
# 주어진 숫자들 중에서 길이 m의 순열을 모두 출력하되
# 같은 숫자가 여러 번 등장할 수 있으므로 중복 순열은 제거해야 한다.

from itertools import permutations

# n = 숫자의 개수, m = 뽑을 숫자의 개수
n, m = map(int, input().split())
nums = list(map(int, input().split()))

# 사전 순으로 출력해야 하므로 먼저 정렬
nums = sorted(nums)

result = []  # 만들어진 모든 순열을 저장할 리스트

# permutations(nums, m)은 nums에서 길이 m짜리 순열을 모두 만들어줌
# 하지만 nums에 중복 숫자가 있으면 같은 순열이 여러 번 생성되므로 나중에 중복 제거 필요
for numbers in permutations(nums, m):
    result.append(numbers)

# 같은 순열이 여러 번 있을 수 있으니 set으로 중복을 제거한 뒤 다시 정렬
# set → 중복 제거 / sorted → 사전 순 정렬
result = sorted(list(set(result)))

for numbers in result:
    for num in numbers:
        print(num, end=' ')
    print()
