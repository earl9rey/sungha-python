# def solution(want, number, discount):
#     answer = 0

#     # 회원가입 가능한 모든 시작 날짜 확인
#     # 10일씩 확인하므로 마지막 시작점은 len(discount) - 10
#     for i in range(len(discount) - 9):

#         # 현재 날짜부터 연속된 10일의 할인 상품
#         ten_days = discount[i:i + 10]

#         # 현재 10일 동안 원하는 상품을 모두 살 수 있는지 확인
#         possible = True

#         # 원하는 상품 하나씩 확인
#         for j in range(len(want)):
#             product = want[j]  # 원하는 상품
#             count = number[j]  # 원하는 상품의 개수

#             # 10일 동안 해당 상품의 개수가 원하는 개수와 다르면 실패
#             if ten_days.count(product) != count:
#                 possible = False
#                 break

#         # 모든 상품의 개수가 조건과 일치하면
#         if possible:
#             answer += 1

#     return answer


# =========================
# 딕셔너리를 사용한 풀이
# =========================

# def solution(want, number, discount):
#     answer = 0
#
#     # 원하는 상품과 개수를 딕셔너리로 만들기
#     # 예: {"banana": 3, "apple": 2, ...}
#     wanted = dict(zip(want, number))
#
#     # 10일 동안 회원가입 가능한 모든 시작 날짜 확인
#     for i in range(len(discount) - 9):
#
#         # 현재 날짜부터 연속된 10일의 할인 상품
#         ten_days = discount[i:i + 10]
#
#         # 현재 10일 동안 할인하는 상품의 개수를 저장할 딕셔너리
#         count = {}
#
#         # 10일 동안 할인하는 상품을 하나씩 확인
#         for product in ten_days:
#
#             # 이미 나온 상품이면 개수 증가
#             if product in count:
#                 count[product] += 1
#
#             # 처음 나온 상품이면 개수를 1로 저장
#             else:
#                 count[product] = 1
#
#         # 원하는 상품과 실제 할인 상품의 개수가 같으면
#         if count == wanted:
#             answer += 1
#
#     return answer


# =========================
# 슬라이딩 윈도우 풀이
# =========================

def solution(want, number, discount):
    answer = 0

    want_dict = {}

    for i in range(len(want)):
        want_dict[want[i]] = number[i]

    discount_dict = {}

    # 처음 10일 상품 개수 세기
    for i in range(10):
        product = discount[i]

        if product in discount_dict:
            discount_dict[product] += 1
        else:
            discount_dict[product] = 1

    # 첫 번째 10일 확인
    if discount_dict == want_dict:
        answer += 1

    # 창을 하루씩 이동
    for i in range(10, len(discount)):

        # 기존 맨 앞 상품 제거
        remove_product = discount[i - 10]
        discount_dict[remove_product] -= 1

        if discount_dict[remove_product] == 0:
            del discount_dict[remove_product]

        # 새로운 상품 추가
        add_product = discount[i]

        if add_product in discount_dict:
            discount_dict[add_product] += 1
        else:
            discount_dict[add_product] = 1

        # 원하는 상품 목록과 비교
        if discount_dict == want_dict:
            answer += 1

    return answer