while True :
    t = input()
    if t == '0' :
        break

    n= len(t)
    p = True

    for i in range(n//2) :
        if t[i] != t[n-i-1] :
            p = False
            break
    
    if p == True :
        print('yes')
    else :
        print('no')

    