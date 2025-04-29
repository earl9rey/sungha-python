# 구현 문제
# p.322 Q-08 문자열 재정렬

s = input()
strList = []
sum = 0

for i in s :
    if i.isdigit() :
        sum += int(i)
    else :
        strList.append(i)
    
strList.sort()
result = ''.join(strList) + str(sum)

print(result)