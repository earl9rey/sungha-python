# 규칙성 : n = 4 부터 P(n) = P(n-2) + P(n-3)

t = int(input())  

for _ in range(t):
    n = int(input()) 

    if n <= 3 : # n = 1, 2, 3일 때 항상 1 출력
        print(1)
        continue
    else :
        p = [0] * (n+1)
        p[1], p[2], p[3] = 1, 1, 1 # n = 3 까지 초기화

        for i in range(4, n+1) :
            p[i] = p[i-2] + p[i-3] # 점화식
    
    print(p[n])




