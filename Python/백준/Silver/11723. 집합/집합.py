# 비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.
# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다.

# [입력] 
# 첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.
# 둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.

# [출력]
# check 연산이 주어질때마다, 결과를 출력한다.

from collections import deque
import sys

setlist = set()

input=sys.stdin.readline # 시간 초과 방지 
n = int(input())

for _ in range(n) :
    s = input().split()

    if s[0] == "add" :
        setlist.add(int(s[1]))

    elif s[0] == "remove" :
        if setlist : 
            setlist.discard(int(s[1]))  
            # remove 대신 discard 사용하면 값이 없어도 에러 X

    elif s[0] == "check" :
        if int(s[1]) in setlist :
            print(1)
        else :
            print(0)

    elif s[0] == "toggle" :
        if int(s[1]) in setlist :
            setlist.remove(int(s[1]))
        else :
            setlist.add(int(s[1]))

    elif s[0] == "all":
        setlist = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                   11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
     
    elif s[0] == "empty":
        setlist = set()
