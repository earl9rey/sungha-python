# 정렬
# p.182 실전 문제 6-4 두 배열의 원소 교체

n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split())) 

a.sort()
b.sort()

def change(a, b) :
    for i in range(k):
        if a[i] < b[n-i-1] :
            a[i], b[n-i-1] = b[n-i-1], a[i]
        else:
            break
        print(a, b)
    
    sum = 0
    for j in range(n) :
        sum += a[j]
    
    return sum

print(change(a,b))