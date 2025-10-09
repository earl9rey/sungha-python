# 최대 힙
import sys
import heapq  # 파이썬 내장 힙(우선순위 큐) 라이브러리

input = sys.stdin.readline 


n = int(input())
heap = []  # 최소 힙을 저장할 리스트 (heapq는 기본적으로 최소 힙 구조 사용)

for _ in range(n):
    x = int(input())

    if x > 0:
        heapq.heappush(heap, -x)  # 자연수가 입력되면, 최소 힙에 -x 추가 (작은 것부터 정렬되므로 부호 바꾸어 추가)
    elif x == 0:
        if len(heap) == 0: 
            print(0)
        else:
            m = heapq.heappop(heap) # 힙에서 가장 작은 원소 (절댓값이 가장 큰 수) 꺼내기
            print(-m) # - 부호 붙여 출력