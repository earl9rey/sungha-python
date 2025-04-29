# 그리디 문제
# p.314 Q-04 만들 수 없는 금액

from itertools import product

n = int(input())
data = list(map(int, input().split()))
data.sort()

coinNum = [list(p) for p in product([0, 1], repeat=n)]
resultList = []

result = 0
for k in coinNum :
    result = 0
    for i in range(n) :
        result += data[i] * k[i]
    resultList.append(result)
    
resultList.sort()
minVal = 1
while True:
    if minVal not in resultList :
        break
    minVal += 1
        

        
print(minVal)