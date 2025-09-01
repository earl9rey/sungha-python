# 김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.

# [입력] 
# 첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다. 
# 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다. 
# 이름은 띄어쓰기 없이 알파벳 소문자로만 이루어지며, 그 길이는 20 이하이다. N, M은 500,000 이하의 자연수이다.
# 듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.

# [출력]
# 듣보잡의 수와 그 명단을 사전순으로 출력한다.

# 시간 초과 ---------------------------------------------
    # import sys
    # input = sys.stdin.readline

    # n, m = map(int, input().split())

    # nheard = [input().strip() for _ in range(n)]
    # nseen = [input().strip() for _ in range(m)]

    # # 듣보잡 찾기 (리스트 탐색)
    # not_heard_and_seen = []
    # for person in nheard:
    #     if person in nseen:
    #         not_heard_and_seen.append(person)

    # # 사전순 정렬
    # not_heard_and_seen.sort()

    # # 출력
    # print(len(not_heard_and_seen))
    # for person in not_heard_and_seen:
    #     print(person)
# ------------------------------------------------------

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nheard = set()
for i in range(n):
    nheard.add(input().rstrip())  # 줄바꿈 제거

nseen = set()
for i in range(m) :
    nseen.add(input().rstrip())   # 줄바꿈 제거

# 듣도 보도 못한 사람 찾기 (집합의 교집합)
result = sorted(list(nheard & nseen)) # 교집합을 리스트로 바꾸고 사전순 정렬

print(len(result))
for i in result :
    print(i)