from collections import deque

def solution(arr):
    queue = deque(arr)
    answer = []
        
    prev = queue.popleft()
    answer.append(prev)
    
    for _ in range(1, len(arr)):
        nxt = queue.popleft()
        
        if nxt != prev :
            answer.append(nxt)
        
        prev = nxt
            
    return answer