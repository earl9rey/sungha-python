def solution(n):
    if n < 3:
        return n
    
    # DP 테이블 초기화 (n=1일 때 1, n=2일 때 2)
    a, b = 1, 2
    
    # 3부터 n까지 반복하며 피보나치 수열 계산
    for _ in range(3, n + 1):
        a, b = b, (a + b) % 1234567
        
    return b