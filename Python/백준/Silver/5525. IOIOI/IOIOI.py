# IOIOI
# cnt = s.count(p) 중첩되는 패턴을 세지 못함 (부분적으로 겹치는 IOIOI 패턴 누락)

# 투 포인터 - 슬라이딩 윈도우 사용 (구글링)


# 시간 초과 --------------------------------------------------------------------

# [문제의 원인]
# s[j:j+3] → 문자열 슬라이싱은 새로운 문자열을 만들기 때문에 반복문 안에서 1,000,000번 하면 느려짐
# 반복문 안에서 계속 슬라이싱 + 비교 → O(m * n) 수준의 연산
# 최악의 경우 문자열 끝까지 검사하면서 내부 while이 계속 반복

    # from collections import defaultdict

    # n = int(input()) # Pn에서의 n값
    # m = int(input()) # 문자열 S의 길이
    # s = input() # I, O로만 이루어진 문자열

    # count = 0          # Pn 패턴 개수를 저장할 변수
    # i = 0              # 문자열 순회를 위한 포인터

    # # 문자열 끝까지 반복 (IOI 패턴은 최소 3글자이므로 m-1까지 확인)
    # while i < m - 1:
    #     if s[i] == 'I':   # 현재 글자가 'I'이면 패턴 가능성 있음
    #         j = i         # 연속 패턴 확인용 포인터
    #         num = 0       # 현재 시작점에서 연속된 "IOI" 패턴 개수 초기화

    #         # 연속된 "IOI" 패턴 확인
    #         while j + 2 < m and s[j:j+3] == "IOI":  # 범위 벗어나지 않고 "IOI" 패턴이면
    #             num += 1     # 연속 패턴 개수 증가
    #             j += 2       # 다음 "IOI" 검사 위치로 이동 (겹치는 패턴 포함)

    #         if num >= n:      # 연속된 IOI 패턴이 n 이상이면
    #             count += num - n + 1   # Pn 패턴 개수 누적 (중첩 패턴 고려)

    #         i = j  # 이미 확인한 범위이므로 포인터를 j로 이동
    #     else:
    #         i += 1  # 시작점이 'I'가 아니면 다음 글자로 이동

    # # 최종 Pn 패턴 개수 출력
    # print(count)
# --------------------------------------------------------------------

# [해결]
# 슬라이싱 대신 문자 비교
# s[j] == 'I' and s[j+1] == 'O' and s[j+2] == 'I' 로 바꿔서 문자열 객체를 새로 만들지 않음
# 연속 패턴 수를 변수로 바로 세기
# j 포인터가 아니라 한 번의 반복문에서 i 포인터만 이동
# 전체 탐색을 한 번만 수행 → O(m) 가능

from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input()) # Pn에서의 n값
m = int(input()) # 문자열 S의 길이
s = input().rstrip()  # I, O로만 이루어진 문자열

count = 0
i = 0
pattern = 0  # 연속된 IOI 패턴 수

while i < m - 1:
    # "IOI" 패턴 확인
    if s[i] == 'I' and s[i+1] == 'O' and i+2 < m and s[i+2] == 'I':
        pattern += 1
        i += 2  # 다음 "IOI" 패턴 확인 (겹치는 부분 포함)
        if pattern >= n:
            count += 1
    else:
        pattern = 0  # 연속 패턴 끊김
        i += 1

print(count)