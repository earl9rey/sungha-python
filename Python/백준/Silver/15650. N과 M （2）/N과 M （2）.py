# N과 M (2)
# 조합 사용

from itertools import combinations

import sys
input = sys.stdin.readline
n, m = map(int, input().split())

data = [0] * n
for i in range(n) :
    data[i] = i+1

comb = combinations(data, m)

for num in comb:
    print(*num)