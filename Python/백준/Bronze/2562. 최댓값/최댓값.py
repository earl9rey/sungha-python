num = []
for i in range(9) :
    n = int(input())
    num.append(n)

maxnum = max(num)
print(maxnum)

for i in range(9) :
    if maxnum == num[i] :
        print(i+1)
        break