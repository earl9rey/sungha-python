# 그리디
# p.92 실전 문제 3-2 큰수의 법칙

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

# 입력 데이터 리스트 정렬
data.sort()

# 가장 큰 수, 두 번째 큰 수 지정
first = data[n-1]
second = data[n-2]

#변수 초기화
isFirst = True # first를 더할 차례인지 아닌지 여부
sum = 0

while m > 0 :
    if (isFirst == True) : # first 더할 차례
        if (m >= k) : # 아직 더해야 하는 횟수가가 k보다 많이 남았을 때
            sum += first * k
            m = m-k
        else : # 더해야 할 횟수가 k보다 적을 때
            sum += first * m
            break           
        isFirst = False  # k를 초과하지 않는 선에서 계산 완료 후 second 더할 차례로 변경
    else :
        sum += second 
        isFirst = True # second는 한 번만 더한 후 다시 first 차례로 변경
        m = m-1

print(sum)
    
