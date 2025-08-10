n = int(input())
num = list(map(int, input().split()))

count = 0
for i in num :
    prime = True

    if i == 1 :
        continue

    for j in range(2, i) :
        if i % j == 0 :
            prime = False
    
    if prime == True :
        count += 1

print(count)