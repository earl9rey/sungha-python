# DFS/BFS
# p.346 Q-18 괄호 변환 

u = []
v = []

def sliceP(p): #문자열을 u와 v로 슬라이싱
    openCount = 0
    closeCount = 0
    
    for i in range(len(p)) :
        if p[i] == '(' :
            openCount += 1
        else :
            closeCount += 1
            
        if openCount == closeCount : # 처음부터 (와 )의 개수를 세서 같아질 때 슬라이싱
            u = p[:i+1]
            v = p[i+1:]
            
            return [u, v]
        

def isRight(p): # 올바른 문자열인지 판단하는 함수
    count = 0
    
    for i in range(len(p)) :
        if p[i] == '(' :
            count += 1  # 먼저 (이면 count 1 증가
        else :
            count -= 1  # )이면 count 1 감소
            
        if count < 0 : # count가 한번이라도 음수가 되면 False (짝이 맞지 않음)
            return False
    
    if count == 0 : # count가 0으로 끝나면 True (짝이 맞음)
        return True
    
    
def reverse(p) : # (이면 )로, )이면 (로 바꿔주는 함수
    result = []
    for s in p: # p의 모든 문자에 대해 전환 
        if s == '(':
            result.append(')')
        else:
            result.append('(')
    return ''.join(result) # 전환한 결과값 합치기 

# 파이썬의 문자열은 immutable(불변) 자료형이라서 이렇게 직접 수정할 수 없음
# 문자열을 수정하려면 새 문자열을 만들어서 대체해야 함

    
def solution(p): 
    if p == "" : # 빈 문자열이면 그대로 반환
        return ""

    result = ""
    
    slice = sliceP(p) #p를 u, v로 쪼개기
    
    if isRight(slice[0]) == True : # 문자열 u가 올바른 문자열이면
        result += slice[0] # 문자열 u는 그대로 두고 
        result += solution(slice[1]) # 문자열 v에 대해 1단계부터 재귀적 수행
        
    else : # 문자열 u가 올바른 문자열이 아니면 
        result += "(" # 빈 문자열에 첫 번째 문자로 '(' 붙이기
        result += solution(slice[1]) # 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열 이어붙이기
        result += ")" # ')'를 다시 붙이기
        result += reverse(slice[0][1:-1]) # 문자열 u의 첫번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙이기
        
    return result # 생성된 문자열 반환
    