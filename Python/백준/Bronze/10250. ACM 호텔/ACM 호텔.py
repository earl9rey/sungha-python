t = int(input())

for _ in range(t) :
    h, w, n = map(int, input().split())

    if n % h == 0 :
        height = h
        width = n // h
    else :
        height = n % h
        width = n // h + 1


    room = int(f"{height}{width:02}")
    print(room)
    


