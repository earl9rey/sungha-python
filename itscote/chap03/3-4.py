# 그리디
# p.99 실전 문제 3-4 1이 될 때까지

n, k = map(int, input().split())

count = 0

while (n >= 1) :
    if (n == 1) : # n이 1이 되면 실행 종료
        break
    if ( n % k == 0) : # n이 k의 배수일 때 나누기
        n = n // k
        count += 1
    else : # n이 k의 배수가 아닐 때 1 빼기
        n = n - 1
        count += 1

print(count)