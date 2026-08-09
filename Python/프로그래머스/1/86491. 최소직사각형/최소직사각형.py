# from itertools import product

# def solution(sizes):
#     answer = float('inf')

#     # 각 명함마다
#     # [가로, 세로] 또는 [세로, 가로]
#     # 두 가지 상태를 저장
#     cards = []

#     for w, h in sizes:
#         cards.append([(w, h), (h, w)])

#     # 모든 회전 조합 생성
#     for case in product(*cards):

#         # 현재 조합에서 필요한 지갑의 가로/세로 계산
#         max_w = max(card[0] for card in case)
#         max_h = max(card[1] for card in case)

#         # 넓이 계산
#         area = max_w * max_h

#         # 최소 넓이 갱신
#         answer = min(answer, area)

#     return answer

def solution(sizes):
    max_width = 0
    max_height = 0

    for w, h in sizes:

        # 큰 값을 가로로 통일
        width = max(w, h)

        # 작은 값을 세로로 통일
        height = min(w, h)

        # 현재까지 필요한 최대 가로 길이 갱신
        max_width = max(max_width, width)

        # 현재까지 필요한 최대 세로 길이 갱신
        max_height = max(max_height, height)

    # 모든 명함을 담을 수 있는 최소 지갑 넓이
    return max_width * max_height