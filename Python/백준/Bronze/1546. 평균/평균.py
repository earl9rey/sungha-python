n = int(input())
score = list(map(int, input().split()))

score.sort()
m = score[-1]
total = 0

for i in score :
    total += i/m*100

print(total / n)

