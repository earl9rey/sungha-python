from itertools import combinations

n, m = map(int, input().split())
num = list(map(int, input().split()))

result = [sum(i) for i in combinations(num, 3)]
result = [j for j in result if j <= m ]

result.sort()
print(result[-1])