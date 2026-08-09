def solution(elements):
    n = len(elements)
    elements = elements * 2

    answer = set()

    for start in range(n):
        # 현재 시작 위치에서의 부분 수열 합
        total = 0

        # 부분 수열의 길이를 1부터 n까지 늘려가며 확인
        for length in range(n):
            # 다음 원소를 하나씩 더함
            total += elements[start + length]

            # 현재까지의 합을 set에 저장
            answer.add(total)

    return len(answer)