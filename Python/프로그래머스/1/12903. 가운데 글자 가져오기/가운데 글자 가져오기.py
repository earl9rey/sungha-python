def solution(s):    
    n = len(s)
    
    if n % 2 == 0:
        answer = s[n//2-1] + s[n//2]
    else:
        answer = s[n//2]
        
        

    return answer