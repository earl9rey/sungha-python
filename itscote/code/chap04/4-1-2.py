# 구현
# p.113 예제 4-2 시각

hour = int(input())
min = 0
sec = 0
        
h = 0
count = 0
while h != hour + 1 :
    for m in range(60) :
        for s in range(60) :
            time = list(str(h)+str(m)+str(s))
            if '3' in time :
                count += 1
    h += 1

print(count)