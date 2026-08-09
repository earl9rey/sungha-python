import math

def solution(n):
    s = math.sqrt(n)
    
    if s.is_integer() :
        answer = (s+1) ** 2
    else:
        answer = -1

    return answer