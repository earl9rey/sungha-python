def solution(n):
    k = 0
    
    while n > 0:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
            k += 1

    answer = k
    
    return answer