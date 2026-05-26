def solution(s):
#     n = [0] * len(s)
    
#     for i in range(len(s)):
#         n[i] = int(s[i])
    n = list(map(int, s.split()))
    
    m = min(n)
    M = max(n)
                                   
    answer = str(m)+" "+str(M)
    return answer