def solution(array, commands):
    answer = []
    
    for c in commands:
        start = c[0]-1
        end = c[1]-1
        idx = c[2]-1
        
        arr = array[start:end+1]
        arr.sort()
        answer.append(arr[idx])
        
    return answer