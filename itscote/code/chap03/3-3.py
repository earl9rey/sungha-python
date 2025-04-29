# 그리디
# p.96 실전 문제 3-3 숫자 카드 게임

n, m = map(int, input().split())

minlist = list()

for i in range(n) :
    data = list(map(int, input().split()))
    minlist.append(min(data)) # 입력 받은 행의 카드 중 가장 작은 수들로 리스트 생성성

maxcard = max(minlist) # 리스트 원소 중 가장 큰 수 저장
     
print(maxcard)       
    

