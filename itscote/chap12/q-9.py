# 구현 문제
# p.323 Q-09 문자열 압축

s = input()
n = len(s) // 2

min_len = len(s)

for jump in range(1, n+1):
    numlist = [s[i:i+jump] for i in range(0, len(s), jump)]
    print(numlist)
    
    result = ""
    prev = numlist[0]
    count = 1
    
    for i in range(1, len(numlist)):
        if numlist[i] == prev:
            count += 1
        else:
            if count > 1:
                result += str(count) + prev
            else:
                result += prev
            prev = numlist[i]
            count = 1
    
    if count > 1:
        result += str(count) + prev
    else:
        result += prev
    
    min_len = min(min_len, len(result))

print(min_len)
