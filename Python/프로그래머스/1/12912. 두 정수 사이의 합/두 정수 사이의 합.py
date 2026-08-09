def solution(a, b):
    answer = 0
    
    if a > b :
        M, m = a, b
    else: 
        M, m = b, a
        
    
    for i in range(m, M+1):
        answer += i
        
    return answer