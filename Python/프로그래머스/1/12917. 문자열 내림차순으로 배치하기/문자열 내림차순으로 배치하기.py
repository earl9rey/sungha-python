from collections import deque

def solution(s):
    up = []
    low = []
    
    for i in (s) :
        if i.isupper() :
            up.append(i)
        else:
            low.append(i)
    
    answer = ''.join(sorted(low, reverse=True) + sorted(up, reverse=True))
            
        
    return answer