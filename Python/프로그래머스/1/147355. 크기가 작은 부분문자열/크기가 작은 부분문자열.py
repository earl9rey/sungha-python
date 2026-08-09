def solution(t, p):
    arr = []
    lenp = len(p)
    
    for i in range(len(t)-len(p)+1):
        new = t[i:i+len(p)]
        
        if int(new) <= int(p) :
            arr.append(new)

    answer = len(arr)
    return answer