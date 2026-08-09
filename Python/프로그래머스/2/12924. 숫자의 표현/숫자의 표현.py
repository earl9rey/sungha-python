# def solution(n):
#     answer = 0

#     # 누적합(시그마) 배열 생성
#     # arr[i] = 1부터 i까지의 합
#     arr = [0]

#     for i in range(1, n + 1):
#         arr.append(i * (i + 1) // 2)

#     # 모든 구간 [i+1 ~ j]의 합 확인
#     for i in range(n):
#         for j in range(i + 1, n + 1):

#             # 구간합 = 1~j의 합 - 1~i의 합
#             # 즉 (i+1) ~ j 의 합
#             if arr[j] - arr[i] == n:
#                 answer += 1

#     return answer

def solution(n):
    answer = 0

    # 시작 숫자
    for start in range(1, n + 1):
        total = 0

        # start부터 연속된 수를 더함
        for num in range(start, n + 1):
            total += num

            # 합이 n이면 경우의 수 추가
            if total == n:
                answer += 1
                break

            # n을 넘어가면 더 볼 필요 없음
            if total > n:
                break

    return answer