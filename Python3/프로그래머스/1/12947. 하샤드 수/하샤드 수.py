def solution(x):
    
    s = str(x)
    sum = 0
    
    for i in s:
        sum += int(i)
    
    if x % sum == 0:
        answer = True
    else:
        answer = False
    
    return answer