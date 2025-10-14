# 회의실 배정

import sys
input = sys.stdin.readline  

n = int(input())            
conf = []                    # 회의 시간 (시작, 끝)을 저장할 리스트

endPoint: int = 0            # 마지막으로 선택한 회의의 종료 시간
answer: int = 0              # 선택된 회의 개수 (최대 회의 수)

# n개의 회의 정보를 입력받음
for _ in range(n):
    s, e = map(int, input().split())  # s: 시작 시간, e: 종료 시간
    conf.append([s, e])               # 회의 정보를 리스트에 추가

# 회의를 '종료 시간' 기준으로 오름차순 정렬
# 종료 시간이 같다면 '시작 시간' 기준으로 오름차순 정렬
conf.sort(key=lambda x: (x[1], x[0]))

# 정렬된 회의들을 순회하며 가능한 회의를 선택
for newStart, newEnd in conf:
    # 현재 회의의 시작 시간이 이전 회의 종료 시간 이후라면 선택 가능
    if endPoint <= newStart:
        answer += 1           # 회의 개수 추가
        endPoint = newEnd     # 현재 회의의 종료 시간을 갱신

# 선택할 수 있는 최대 회의 개수 출력
print(answer)
