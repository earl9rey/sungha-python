#5430 AC

import ast
from collections import deque

T = int(input())

for _ in range(T) :
    p = input()
    n = int(input())
    arr = deque(ast.literal_eval(input()))

    rCount = 0
    error = False

    for i in p :
        # D일 때
        if i == 'D' :
            if len(arr) == 0 :
                print("error")
                error = True
                break

            if rCount % 2 == 0 : # rCount가 짝수면 입력된 순서 그대로 (앞에서 삭제)
                arr.popleft()
            else: # rCount가 홀수면 뒤집힌 상태 (뒤에서 삭제)
                arr.pop()

        # R일 때
        else :
            rCount += 1

    if not error:  # 에러 없을 때만 출력
        if rCount % 2 == 0:
            print('[' + ','.join(map(str, arr)) + ']')
        else:
            arr.reverse()
            print('[' + ','.join(map(str, arr)) + ']')

