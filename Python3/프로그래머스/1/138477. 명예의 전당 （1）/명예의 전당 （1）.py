def solution(k, score):
    answer = []
    
    for i in range(len(score)):
        current = score[:i+1]
        min_score = min(sorted(current)[-k:])
        
        answer.append(min_score)
                
    
    return answer