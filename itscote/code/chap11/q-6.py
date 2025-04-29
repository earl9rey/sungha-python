# 그리디 문제
# p.316 Q-06 무지의 먹방 라이브

def solution(food_times, k):
    next = 0
    count = 0
    answer = 0
    
    while count < k :
        if all(x == 0 for x in food_times):
            answer = -1 
            break
        else :
            if next < len(food_times) - 1 :
                if food_times[next] > 0 :
                    food_times[next] -= 1
                    count += 1
                    next += 1
                else :
                    next += 1
            elif next == len(food_times) - 1:
                if food_times[next] > 0 :
                    food_times[next] -= 1
                    count += 1
                    next = 0
                else :
                    next = 0
    
    if answer != -1 :
        for i in range(len(food_times)) :
            if food_times[next] > 0 :
                answer = next + 1
            else :
                next += 1
        
        
    return answer