# 그리디
# p.87 예제 3-1 거스름돈

n = int(input())

# 변수 초기화
coin = [500, 100, 50, 10]
result = 0

for i in coin :
    result += n // i # 각 동전 개수
    n = n % i # 아직 남은 (더 지불해야 하는) 금액
    
print(result)
