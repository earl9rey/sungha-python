# 다이나믹 프로그래밍
# p.220 실전 문제 8-3 개미 전사

n = int(input())
array = list(map(int, input().split()))

# 계산된 결과를 저장하기 위한 리스트
d = [0] * 100

# 다이나믹 프로그래밍 (보텀업)
d[0] = array[0]               # 첫 번째 창고는 무조건 털고
d[1] = max(array[0], array[1])  # 두 번째 창고는 더 큰 쪽만

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + array[i])  # 현재 창고를 털지 말지 결정

print(d[n-1])  # n번째 창고까지의 최대 식량
