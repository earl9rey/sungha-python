a, b = map(int, input().strip().split(' '))

sqr = ["*"] * a

for i in range(b):
    print("".join(sqr))