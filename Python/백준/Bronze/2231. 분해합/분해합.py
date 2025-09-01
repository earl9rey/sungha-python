n = int(input())
find = False

for m in range(n) :
    result = m
    s = str(m)
    for i in range(len(s)) :
        result += int(s[i])

    if result == n :
        find = True
        print(m)
        break

if find == False :
    print(0)
