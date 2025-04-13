# 그리디 문제
# p.315 Q-05 볼링공 고르기

n, m = map(int, input().split())
weight = list(map(int, input().split()))


# 변수 초기화
all = n * (n-1) // 2 # 전체 경우의 수
comp = 0 # 여사건 (같은 무게의 공 선택) 경우의 수 
result = 0


# 각 조합에서의 무게가 같은 공 개수 리스트 (combi) 계산
combi = list()

weight.sort() # 공 무게 리스트 정렬 후 사용
w = weight[0]
count = 0

for i in weight :
    if (w == i) :
        count += 1
        w = i
        continue
    else :
        combi.append(count)
        count = 1
        w = i
        continue

combi.append(count)


# 여사건 (comp) 계산
for j in combi :
    comp += j * (j-1) // 2

# 무게가 다른 볼링공을 고르는 경우의 수 계산 (전체 - 여사건)
result = all - comp

print(result)