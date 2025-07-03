# 정렬 문제
# p.363 Q-26 카드 정렬하기

n = int(input())
num = [int(input()) for _ in range(n)]

num.sort()

def calc(lst) :
    if len(lst) <= 1:
        return 0
    
    sum = lst[0] + lst[1]
    lst = lst[2:]
    lst.insert(0, sum)

    return sum + calc(lst)


print(calc(num))