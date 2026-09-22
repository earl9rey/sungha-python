def solution(clothes):
    d = dict()
    
    
    for i in range(len(clothes)):
        kind = clothes[i][1]

        if kind not in d:
            d[kind] = 1
        else:
            d[kind] += 1
        
    
    # 각 종류에서 "안 입기"까지 포함해서 경우의 수 계산
    answer = 1

    for count in d.values():
        answer *= (count + 1)

    # 아무것도 안 입는 경우 제외
    answer -= 1
    
    return answer