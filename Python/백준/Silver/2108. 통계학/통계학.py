# 수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.
    # 산술평균 : N개의 수들의 합을 N으로 나눈 값
    # 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
    # 최빈값 : N개의 수들 중 가장 많이 나타나는 값
    # 범위 : N개의 수들 중 최댓값과 최솟값의 차이
# N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

# [입력] 
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 단, N은 홀수이다. 
# 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.

# [출력]
# 첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
# 둘째 줄에는 중앙값을 출력한다.
# 셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
# 넷째 줄에는 범위를 출력한다.

import sys
import math
from collections import Counter

input = sys.stdin.readline

n = int(input())
count = [0] * 8001  # -4000 ~ 4000
numlst = []

for _ in range(n):
    num = int(input())
    numlst.append(num)
    count[num + 4000] += 1  # 값 → 인덱스로 매핑해서 카운팅

# 1. 산술평균
avg = round(sum(numlst) / n)

# 2. 중앙값 (정렬 필요)
numlst.sort()
center = numlst[n // 2]

# 3. 최빈값
maximum = max(count)  # count 배열에서 가장 큰 값(=최대 빈도수)을 구함
modes = [i - 4000 for i, c in enumerate(count) if c == maximum]
# count 배열에서 값이 max_freq인 모든 인덱스를 찾음
# i는 0~8000 범위이므로 실제 값으로 변환하려면 i - 4000 해줘야 함
# (예: count[4001] = 2 → 실제 값은 1이 2번 등장했다는 뜻)


# 최빈값이 여러 개라면 정렬 후 "두 번째로 작은 값"을 선택 (문제 조건)
if len(modes) > 1: 
    mode = sorted(modes)[1]
# 최빈값이 하나뿐이라면 그대로 선택
else:
    mode = modes[0]

# 4. 범위
r = max(numlst) - min(numlst)

print(avg)
print(center)
print(mode)
print(r)