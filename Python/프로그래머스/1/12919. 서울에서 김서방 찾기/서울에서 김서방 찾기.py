def solution(seoul):
    x = 0
    
    for i in range(len(seoul)):
        if seoul[i] == "Kim" :
            x = i
            break
    
    answer = "김서방은 "+str(x)+"에 있다"
    
    return answer