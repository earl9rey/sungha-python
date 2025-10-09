# 시간 초과 -------------------------------------
    # n, m = map(int, input().split())

    # nlist = list(map(int, input().split()))
    # mlist = []

    # for _ in range(m) :
    #     i, j = map(int, input().split())  
    #     result = nlist[i-1 : j] # 리스트 슬라이싱

    #     print(sum(result))
# --------------------------------------------



# 시간 초과 2 -------------------------------------------------------  
    # DP (다이나믹) - 누적 합 미리 계산해 저장해놓기

    # n, m = map(int, input().split())
    # nlist = list(map(int, input().split()))

    # sum = 0
    # sumlist = []

    # for i in nlist :
    #     sum += i
    #     sumlist.append(sum)  # 현재까지 누적 합 저장

    # for _ in range(m) :
    #     i, j = map(int, input().split())  
    #     if i == 1 :
    #         result = sumlist[j-1] # 1번부터 j번까지 합
    #     else :
    #         result = sumlist[j-1] - sumlist[i-2] # i~j까지 합
    #     print(result)

# -----------------------------------------------------------------

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nlist = list(map(int, input().split()))

sum = 0
sumlist = [0] * (n+1) # 미리 테이블 초기화

for i in range(1,n+1):
    sumlist[i]= sumlist[i-1] + nlist[i-1] # 합 미리 구해 저장

for _ in range(m) :
    i, j = map(int, input().split())  
    result = sumlist[j] - sumlist[i-1] # i~j까지 합
    
    print(result)