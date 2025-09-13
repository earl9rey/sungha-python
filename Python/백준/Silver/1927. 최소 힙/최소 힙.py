# 최소 힙

# 시간 초과 --------------------------------------------------------
    # import heapq  # 파이썬 내장 힙(우선순위 큐) 라이브러리

    # n = int(input())
    # heap = []  # 최소 힙을 저장할 리스트 (heapq는 기본적으로 최소 힙 구조 사용)

    # for _ in range(n):
    #     x = int(input())

    #     if x > 0:
    #         heapq.heappush(heap, x)  # 자연수가 입력되면, 최소 힙에 추가
    #     elif x == 0:
    #         if len(heap) == 0: 
    #             print(0)
    #         else:
    #             m = heapq.heappop(heap) # 힙에서 가장 작은 원소 꺼내기
    #             print(m)
# -----------------------------------------------------------------


import sys
import heapq  # 파이썬 내장 힙(우선순위 큐) 라이브러리

input = sys.stdin.readline # 제발 습관화할 것


n = int(input())
heap = []  # 최소 힙을 저장할 리스트 (heapq는 기본적으로 최소 힙 구조 사용)

for _ in range(n):
    x = int(input())

    if x > 0:
        heapq.heappush(heap, x)  # 자연수가 입력되면, 최소 힙에 추가
    elif x == 0:
        if len(heap) == 0: 
            print(0)
        else:
            m = heapq.heappop(heap) # 힙에서 가장 작은 원소 꺼내기
            print(m)