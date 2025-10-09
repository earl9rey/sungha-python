# 절댓값 힙

# 시간 초과 --------------------------------------------------------------------

    # import heapq

    # n = int(input())
    # arr = [] # x 값을 저장할 배열 
    # heap = [] # x의 절댓값을 저장할 힙

    # for _ in range(n) :
    #     x = int(input())

    #     # x가 0일 때 - 절댓값 출력
    #     if x == 0 : 
    #         if len(arr) == 0 : # 배열이 비어있다면 0 출력
    #             print(0)
    #         else: # 배열이 비어있지 않다면
    #             m = heapq.heappop(heap) # 힙에서 가장 작은 절댓값 하나 뽑아내기
    #             if -m in arr : # 만약 배열에 음수로 존재한다면 (음수가 더 작으므로)
    #                 arr.remove(-m) # 배열에서도 음수 제거
    #                 print(-m)
    #             else : # 만약 배열에 음수로 존재하지 않는다면 (양수만 존재하므로)
    #                 arr.remove(m) # 배열에서 양수 (절댓값 그대로) 제거
    #                 print(m) 

    #     # x가 0이 아닐 때 - x값 추가 
    #     else: 
    #         arr.append(x) # 배열에 x 값 저장 
            
    #         if x < 0 : # 만약 x가 음수라면 
    #             heapq.heappush(heap, -x) # 힙에는 - 부호 붙여서 절댓값으로 저장
    #         else : # x가 양수라면
    #             heapq.heappush(heap, x) # 힙에 그대로 저장
 # ---------------------------------------------------------------------------

# 힙을 튜플로 구성할 것!

import sys
import heapq

n = int(input())
heap = []

for _ in range(n):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, (abs(num), num)) # heap = [(절댓값, 실제 값), ... ]
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)