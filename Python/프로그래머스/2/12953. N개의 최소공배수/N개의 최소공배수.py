def solution(arr):
    max_num = max(arr)
    n = 1

    while True:
        num = max_num * n

        # arr의 모든 숫자로 나누어지는지 확인
        if all(num % x == 0 for x in arr):
            return num

        n += 1