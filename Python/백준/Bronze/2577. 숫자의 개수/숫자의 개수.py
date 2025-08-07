a = int(input())
b = int(input())
c = int(input())


num = str(a * b * c)
numlst = [0]*10

for i in num :
    numlst[int(i)] += 1


for i in numlst :
    print(i)