# 그리디 문제
# p.311 Q-01 모험가 길드

n = int(input())
data = list(map(int, input().split()))

# 입력 리스트 정렬
data.sort()

# 변수 초기화
num = data[0] # 데이터의 각 원소
count = 0 # 각 숫자의 개수
countlist = list() # 각 숫자 개수 리스트

# 각 숫자 개수 리스트 (countlist) 계산 및 생성
for i in data :
    if (num == i) :
        count += 1
        continue
    else :
        countlist.append(count)
        count = 1
        num = i
        continue

countlist.append(count)

# 변수 초기화
k = 0
rem = 0 # 나머지
result = 0

# 묶을 수 있는 그룹 개수 계산
for j in countlist :
    k += j #count 원소 값을 더해 num 값에 들어갈 data 리스트의 인덱스 계산 과정 (k-1)
    num = data[k-1]
    count = j
    
    result += (count + rem) // num
    rem = (count + rem) % num 

print(result)