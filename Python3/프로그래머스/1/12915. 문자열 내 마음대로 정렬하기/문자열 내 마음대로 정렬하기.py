def solution(strings, n):
    strings.sort()
    
    arr = []
    for s in strings:
        arr.append([s[n], s])
    
    arr.sort(key=lambda x: x[0])
    answer = [x[1] for x in arr]
    
    return answer