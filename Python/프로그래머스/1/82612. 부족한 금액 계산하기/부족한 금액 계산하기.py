def solution(price, money, count):
    answer = -1
    sum = 0
    
    for i in range(1, count+1):
        sum += i
    
    total = price * sum
    answer = total - money
    
    if answer > 0 :
        return answer
    else:
        return 0
