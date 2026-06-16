def solution(s):
    answer = []
    
    for i in range(len(s)):
        idx = s[:i].rfind(s[i]) # 뒤에서 셀 때 첫번째 등장 위치
        
        if idx == -1:
            answer.append(-1)
        else:
            answer.append(i - idx)
            
    return answer