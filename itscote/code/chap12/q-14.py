# 구현 문제
# p.335 Q-14 외벽 점검

from itertools import permutations
#dist에 있는 친구들을 모든 가능한 순서대로 배치하기 위해 permutations() 사용.
#친구마다 커버할 수 있는 거리가 다르므로, 순서에 따라 결과가 달라짐.


def solution(n, weak, dist):
    length = len(weak)
    weak_extended = weak + [w + n for w in weak]     # 외벽은 원형이므로, 탐색을 쉽게 하기 위해 선형 배열처럼 늘림 (한 방향 탐색)
    answer = len(dist) + 1  # 친구 수의 최댓값 + 1 (불가능한 경우 대비)

    for friends in permutations(dist):    # 친구 순열을 모두 시도
        for start in range(length):       # 모든 시작점에 대해 시도
            count = 1  # 첫 번째 친구 투입
            
            # 첫 번째 친구가 커버할 수 있는 범위 (시작점을 기준으로 어디까지 갈 수 있는가?)
            position = weak_extended[start] + friends[count - 1]

            # 시작점부터 차례대로 점검
            for idx in range(start, start + length):
                if weak_extended[idx] > position: # 현재 친구가 커버할 수 없는 지점이 나오면 (커버 범위보다 위치값이 커지면)
                    count += 1             # 다음 친구 투입
                    if count > len(dist):  # 더 이상 친구 없으면 break 
                        break
                     
                    # 다음 친구의 커버 범위 갱신 (현재 지점을 기준으로 어디까지 갈 수 있는가?)
                    position = weak_extended[idx] + friends[count - 1]
            else:
                # 모든 weak 지점을 점검 완료했을 경우
                answer = min(answer, count)

    # 불가능한 경우
    if answer > len(dist):
        return -1
    return answer