n, k = map(int, input().split())

numerator = 1
denominator = 1

for i in range(k) :
    numerator *= n
    n = n-1
    denominator *= i+1

print(numerator//denominator)