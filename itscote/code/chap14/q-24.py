# 정렬 문제
# p.360 Q-24 안테나

n = int(input())
house = list(map(int, input().split()))

house.sort(reverse=True) # 집 위치 큰 것부터 나열
print(house)

def distance(house, antenna) :
    sum = 0

    for i in house : # 모든 집 위치에 대해
        sum += abs(antenna - i) # 주어진 안테나까지의 거리를 구한 후 합산
    
    return [antenna, sum] # 안테나 위치와 거리의 총합 반환

result = []

# 집 위치 중 가장 큰 값을 안테나 위치 최대값으로 설정 
for antenna in range(house[0]) : # 안테나가 위치할 수 있는 모든 위치에 대해
    result.append(distance(house, antenna+1)) # 안테나, 거리 총합 값을 리스트에 추가

result = sorted(result, key=lambda x: x[1]) # 거리 총합이 작은 순서대로 정렬

print(result[0][0]) # 정렬된 첫 번째 원소 중 안테나 위치 값