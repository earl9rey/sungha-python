t = int(input())

for _ in range(t) :
    s = input()
    count = 0
    score = 0
    
    for i in s :
        if i == 'O' :
            count += 1
            score += count
        else :
            count = 0
    print(score)