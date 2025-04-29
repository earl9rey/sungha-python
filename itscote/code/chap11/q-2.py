# 그리디 문제
# p.312 Q-02 곱하기 혹은 더하기

s = input()
result = 0
prev = 0

for i in s :
    num = int(i)
    if (num == 0 or prev == 0) :
        result += num
    else : 
        result *= num
    prev = num
    
print(result)