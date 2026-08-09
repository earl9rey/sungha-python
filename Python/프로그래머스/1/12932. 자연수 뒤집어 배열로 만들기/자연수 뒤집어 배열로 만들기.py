from collections import deque

def solution(n):    
    s = str(n)
    d = deque()
    
    
    for i in s:
        d.appendleft(int(i))
    
    answer = list(d)
    
    
    return answer