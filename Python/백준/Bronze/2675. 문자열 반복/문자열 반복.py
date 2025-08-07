t = int(input())

for _ in range(t):
    n, s = input().split() 
    n = int(n)         

    result = []
    for i in s:
        result.append(i * n)

    print(''.join(result)) 