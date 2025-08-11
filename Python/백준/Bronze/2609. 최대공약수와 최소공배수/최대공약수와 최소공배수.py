a, b = map(int, input().split())

M = max(a, b)
m = min(a, b)

for i in range(m, 0, -1) :
    if a % i == 0 and b % i == 0 :
        gcd = i
        break

lcm = gcd * (a // gcd) * (b // gcd)

print(gcd)
print(lcm)


