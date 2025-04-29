# 구현 문제
# p.325 Q-10 자물쇠와 열쇠

def solution(key, lock):
    n = len(lock)  # 자물쇠 크기
    m = len(key)   # 열쇠 크기

    # 90도 회전 함수 (시계 방향)
    def rotate(matrix):
        n = len(matrix)
        rotated = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                rotated[j][n - 1 - i] = matrix[i][j]
        return rotated

    # 4번(0도, 90도, 180도, 270도) 돌면서 확인
    for _ in range(4):
        key = rotate(key)  # 열쇠를 90도 회전시킴

        # 열쇠를 자물쇠 위로 옮겨가면서 일일이 확인
        for x in range(-m + 1, n):
            for y in range(-m + 1, n):
                success = True  # 성공 여부 초기화

                # 자물쇠 복사해서 결과 확인용 리스트 만들기
                result = [row[:] for row in lock]

                # 현재 (x, y) 위치에 열쇠를 놓아봄
                for i in range(m):
                    for j in range(m):
                        ni = i + x  # 자물쇠의 행 위치
                        nj = j + y  # 자물쇠의 열 위치

                        # 열쇠가 자물쇠 범위 안에 들어가야만 더하기
                        if 0 <= ni < n and 0 <= nj < n:
                            result[ni][nj] += key[i][j]

                # 자물쇠가 모두 1이 되어야 성공
                for i in range(n):
                    for j in range(n):
                        if result[i][j] != 1:
                            success = False
                            break
                    if not success:
                        break

                if success:
                    return True  # 열 수 있으면 바로 종료

    return False  # 4번 회전하고 다 해봤는데 안되면 False
