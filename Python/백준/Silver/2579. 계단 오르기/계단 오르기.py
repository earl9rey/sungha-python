# 다이나믹 프로그래밍 - 구글링

n = int(input()) # 계단 개수
s = [int(input()) for _ in range(n)] # 계단 리스트

dp=[0]*(n) # dp 리스트

if len(s) <= 2: # 계단이 2개 이하일땐 그냥 다 더해서 출력
    print(sum(s))

else: # 계단이 3개 이상일 때
    dp[0]=s[0] # 첫째 계단 계산
    dp[1]=s[0]+s[1] # 둘째 계단까지 계산

    for i in range(2,n): # 3번째 계단부터 dp 점화식 이용

        # 2계단을 연속으로 밟은 경우 & 1계단을 건너뛴 경우 비교 -> 최댓값 갱신
        dp[i] = max(dp[i-3]+s[i-1]+s[i], dp[i-2]+s[i]) 

    print(dp[-1])