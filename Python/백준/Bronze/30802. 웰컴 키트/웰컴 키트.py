n = int(input())
s, m, l, xl, xxl, xxxl = map(int, input().split())
t, p = map(int, input().split())

print((s-1)//t + (m-1)//t + (l-1)//t + (xl-1)//t + (xxl-1)//t + (xxxl-1)//t + 6)
print(n // p, end=" ")
print(n%p)