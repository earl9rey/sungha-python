# n = 1 -> 답 1
# n = 2 -> 답 2
# n = 3 -> 답 4
# n = 4 -> 답 7
# n = 5 -> 답 13
# n = 6 -> 답 24
# n = 7 -> 답 44
# ...
# [규칙성] 이전 3개의 값을 더하면 답!

t = int(input())

for _ in range(t) :
    n = int(input())

    if n == 1: # n이 3보다 작은 경우 바로 출력
        print(1)
        continue
    elif n == 2:
        print(2)
        continue
    elif n == 3:
        print(4)
        continue

    count = [0] * (n+1)
    count[1] = 1
    count[2] = 2
    count[3] = 4 # n = 3 까지만 초기화

    for i in range(4, n+1) :
        count[i] = count[i-3] + count[i-2] + count[i-1] # 점화식
    
    print(count[n])