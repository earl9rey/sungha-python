# def solution(d, budget):
#     answer = len(d)
        
#     if budget > sum(d):
#         return answer

#     d.sort(reverse=True)
    
    
#     for i in d:
#         if budget > sum(d) - i :
#             answer = answer-1
#             break
#         else:
#             answer = answer-1
#             continue

#     return answer

def solution(d, budget):
    d.sort()

    count = 0
    total = 0

    for money in d:
        total += money

        if total > budget:
            break

        count += 1

    return count