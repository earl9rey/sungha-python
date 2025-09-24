# 과일 탕후루

# 시간 초과 (set 사용) -------------------------------------------

    # import sys
    # input = sys.stdin.readline

    # n = int(input())
    # s = list(map(int, input().split()))

    # # checkTwo 함수: 주어진 구간 s 안의 과일 종류가 2가지 이하인지 확인
    # def checkTwo(s):
    #     if len(set(s)) <= 2:       # set()을 쓰면 중복 제거된 과일 종류 개수를 알 수 있음
    #         return True            # 과일 종류가 2개 이하이면 True
    #     else:
    #         return False           # 아니면 False

    # if len(set(s)) == n : # [추가] 이미 두 종류 이하의 과일로 이루어져 있을 때
    #     print(n)
    #     exit()

    # maxL = 0                        # 최대 길이를 저장할 변수 
    # for a in range(0, n+1):        # a는 앞에서 잘라낼 개수 (0 ~ n)
    #     for b in range(0, n-a+1):  # b는 뒤에서 잘라낼 개수 (0 ~ n-a)
    #         # 부분 구간: 앞에서 a개, 뒤에서 b개를 잘라내고 남은 부분
    #         if checkTwo(s[a:n-b]) == True:   # 남은 부분에서 과일 종류가 2개 이하라면
    #             if maxL < n-a-b:              # 지금까지 최대 길이보다 크다면 갱신
    #                 maxL = n-a-b     
            
    # print(maxL)

# ------------------------------------------------------------

# 구글링 - 투 포인터 (dictionary 사용)

from collections import defaultdict

n = int(input())                         # 과일 개수 n 입력
fruit = list(map(int, input().split()))  # 과일 종류 배열 입력

s, e = 0, 0                              # 투 포인터 시작(s)과 끝(e)
count = defaultdict(int)                 # 구간 내 과일 종류별 개수 저장
max_count = 0                            # 조건(2가지 이하)을 만족하는 최대 길이 저장

# e 포인터를 오른쪽으로 확장하면서 탐색
while e < n:
    count[fruit[e]] += 1                 # 새로운 과일 추가
                                         # (해당 종류 개수를 +1)

    # 과일 종류가 2개를 초과하면, s 포인터를 오른쪽으로 이동
    while len(count.keys()) > 2:
        count[fruit[s]] -= 1             # s 위치 과일 개수 줄이기
        if count[fruit[s]] == 0:         # 만약 개수가 0이 되면
            del count[fruit[s]]          # 딕셔너리에서 해당 과일 삭제
        s += 1                           # 왼쪽 포인터 한 칸 이동

    e += 1                               # 오른쪽 포인터 한 칸 이동

    # 현재 구간 [s, e) 의 총 길이 갱신
    max_count = max(max_count, sum(count.values()))

# 최종 결과 출력
print(max_count)
