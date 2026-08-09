def solution(people, limit):
    heavy = len(people)-1
    light = 0
    count = 0
    
    people.sort()
    
    while heavy >= light:
        if people[heavy] + people[light] <= limit:
            heavy -= 1
            light += 1
        else:
            heavy -= 1
        count += 1
            
    answer = count
    
    return answer