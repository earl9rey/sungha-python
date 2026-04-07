# 1932 정수 삼각형 (dp)

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
d = []

for i in range(n):
  d.append(list(map(int, input().split())))


for i in range(1,n):
  for j in range(len(d[i])):

    # 왼쪽 끝(j == 0)
    # 오른쪽 위 대각선(j)가 존재함
    if j==0:
      d[i][j] = d[i][j] + d[i-1][j]


    # 오른쪽 끝(j == i)
    # 왼쪽 위 대각선(j-1)이 존재함
    elif j==len(d[i])-1: 
      d[i][j] = d[i][j] + d[i-1][j-1]


    # 가운데(j가 0도 아니고 끝도 아님)
    # 오른쪽(j)과 왼쪽(j-1) 위 대각선 중 큰 값 선택
    else:
      d[i][j] = max(d[i-1][j-1], d[i-1][j]) + d[i][j]


# 마지막 줄(d[n-1])에는 삼각형 꼭대기부터 내려왔을 때 만들 수 있는 최대 합들이 저장되고, 그 중 최댓값 출력
print(max(d[n-1]))