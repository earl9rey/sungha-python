# 1629 곱셈 (분할 정복)

# 시간 초과 -----------------------------
    # import sys
    # input = sys.stdin.readline

    # A, B, C = map(int, input().split())
    # result = 1

    # for _ in range(B) :
    #     if result * A < C :
    #         result = result * A
    #     else :
    #         result = (result * A) % C

    # print(result)
# -----------------------------------


import sys
input = sys.stdin.readline

# A^B % C 를 분할 정복 방식으로 계산하는 함수
def calc(A, B, C) :

    # A^1 % C = A % C 이므로 종료 
    if B == 1:
        return A % C

    # A^(B//2) 를 먼저 계산 (반으로 쪼개는 분할 정복 핵심)
    X = calc(A, B // 2, C)

    # B가 짝수인 경우
    # A^B = (A^(B/2))^2
    if B % 2 == 0:
        return (X * X) % C

    # B가 홀수인 경우
    # A^B = A * (A^(B//2))^2
    else:
        return (A * X * X) % C


A, B, C = map(int, input().split())
print(calc(A, B, C))





