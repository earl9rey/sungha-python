# N과 M (5)
# 순열 사용

from itertools import permutations

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

comb = permutations(data, m)

for num in comb:
    print(*num)