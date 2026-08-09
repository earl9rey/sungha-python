from collections import Counter

def solution(k, tangerine):
    count = Counter(tangerine) # {원소: 원소 개수} 형태로 만들어줌
    counts = sorted(count.values(), reverse=True) # 큰 것부터 정렬

    answer = 0

    for c in counts:
        k -= c
        answer += 1
        
        if k <= 0:
            break

    return answer
