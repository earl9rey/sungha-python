t = int(input())
result = []

for _ in range(t) :
    c1, c2 = map(int, input().split())
    case = c1 + c2
    result.append(case)

for i in result :
    print(i)
