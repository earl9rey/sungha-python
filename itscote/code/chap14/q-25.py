# 정렬 문제
# p.361 Q-25 실패율 (시간 초과) https://school.programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    result = []
    answer = []
    for i in range(N) :
        n = sum(1 for x in stages if x == i+1) # if 문의 조건에 맞는 배열 원소의 개수 찾기 (1씩 더해가며)
        d = sum(1 for x in stages if x >= i+1)
        
        if d == 0 :
            fail = 0
        else:
            fail = n / d
        
        result.append([i+1, fail])
        
    result.sort(key=lambda x: -x[1])      
    
    for j in result:
        answer.append(j[0])
        
    return answer