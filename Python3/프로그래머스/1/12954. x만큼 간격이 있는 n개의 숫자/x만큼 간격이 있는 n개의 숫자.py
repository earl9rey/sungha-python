def solution(x, n):
    answer = []
    i = x
    
    for _ in range(n):
        answer.append(x)
        x = x + i
    return answer