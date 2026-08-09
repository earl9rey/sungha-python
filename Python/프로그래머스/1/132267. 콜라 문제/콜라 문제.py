def solution(a, b, n):
    answer = 0

    while n >= a:
        exchange = n // a     
        answer += exchange * b 
        n = exchange * b + (n % a)

    return answer