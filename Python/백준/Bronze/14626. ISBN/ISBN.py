n = input()

sum = 0
index = -1

for i in range(len(n)) :
    if n[i].isdigit() :
        if i % 2 == 0 :
            sum += int(n[i])
        else :
            sum += int(n[i]) * 3
    else :
        index = i

num = 0 

for j in range(10) :
    newsum = sum
    if index % 2 == 0 :
        newsum += j
    else :
        newsum += j * 3
    
    if newsum % 10 == 0 :
        num = j
        break
    

print(num)

