# A -> B

a, b = map(int, input().split())

def calc_1(n) :
    return n * 2

def calc_2(n) :
    return 10 * n + 1

def dfs(n, count):
    if n == b:
        return count

    # 초과 시 실패 처리
    if n > b:
        return -1

    # 왼쪽 탐색
    left = dfs(calc_1(n), count + 1)
    if left != -1:
        return left

    # 오른쪽 탐색
    right = dfs(calc_2(n), count + 1)
    return right  # 못 찾으면 자동으로 -1이 올라감

result = dfs(a, 0)

if result == -1 :
    print(result)
else:
    print(result + 1)
