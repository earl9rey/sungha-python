# 구현 문제
# p.321 Q-07 럭키 스트레이트

num = int(input())
num = str(num)

n = len(num) // 2
left = 0
right = 0

for i in range(n) :
    left += int(num[i])
    right += int(num[i+n])

if left == right :
    print('LUCKY')
else :
    print('READY')