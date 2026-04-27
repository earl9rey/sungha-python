def solution(n):
    l = list(str(n))
    s = sorted(l, reverse=True)
    
    answer = int("".join(s))
    
    
    return answer