n = int(input())

k = 0
while True :
    if n <= 3 * k * (k + 1) + 1:
        print(k + 1)
        break
    k = k+1
    