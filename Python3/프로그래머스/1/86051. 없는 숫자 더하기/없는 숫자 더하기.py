def solution(numbers):
    numberSet = set(numbers)
    answer = 0
    
    for i in range(0, 10):
        if i in numberSet:
            continue
        else:
            answer += i

    return answer