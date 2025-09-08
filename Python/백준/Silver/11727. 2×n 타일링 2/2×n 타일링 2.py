# DP (다이나믹 프로그래밍)

n = int(input())

if n == 1 :
    print(1)
    exit()
elif n == 2 :
    print(3)
    exit()
else :
    dp = [0] * (n+1)
    dp[1], dp[2] = 1, 3

for i in range(3, n+1) :
    dp[i] =  (dp[i-1] + dp[i-2] * 2)  % 10007 # 점화식

print(dp[n])