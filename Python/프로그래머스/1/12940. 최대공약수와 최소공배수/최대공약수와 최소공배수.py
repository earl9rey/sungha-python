def solution(n, m):
    a, b = n, m
    
    while b:
        a, b = b, a % b
    
    gcd = a
    lcm = n * m // gcd
    
    return [gcd, lcm]

# from math import gcd

# def solution(n, m):
#     g = gcd(n, m)
#     return [g, n * m // g]