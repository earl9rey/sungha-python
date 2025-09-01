while True:

    num = list(map(int, input().split()))

    num.sort()

    a = num[0]
    b = num[1]
    c = num[2]

    if a == 0 and b == 0 and c == 0 :
        break

    if a**2 + b**2 == c**2 :
        print("right")
    else :
        print("wrong")