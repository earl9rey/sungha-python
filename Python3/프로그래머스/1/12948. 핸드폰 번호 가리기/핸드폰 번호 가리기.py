def solution(phone_number):
    n = len(phone_number)
    last = phone_number[n-4:]
    
    answer = "*" * (n-4) + last
    
    return answer