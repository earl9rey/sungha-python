from collections import Counter

def solution(nums):
    count = Counter(nums)
    
    if len(nums)//2 > len(count) :
        return len(count)
    else:
        return len(nums)//2