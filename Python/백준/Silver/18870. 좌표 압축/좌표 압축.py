# 좌표 압축

# 시간 초과 1 (직접 세기) ---------------------- ----------------------
    # import sys
    # input = sys.stdin.readline

    # n = int(input())
    # x = list(map(int, input().split()))

    # result = [0] *  n

    # for i in range(n) :
    #     count = 0
        
    #     for j in x :
    #         if x[i] > j :
    #             count += 1
        
    #     result[i] = count

    # print(result)

# ------------------------------------------------------------

# 시간 초과 2 (정렬 후 인덱스 비교) ---------------------------------------------

    # import copy
    # import sys
    # input = sys.stdin.readline

    # n = int(input())
    # x = list(map(int, input().split()))

    # compare = sorted(set(x)) # 중복 제거 및 정렬

    # 중복 제거 후 정렬된 리스트에서의 인덱스가 좌표 압축 결과  
    # for i in x :
    #     print(compare.index(i), end=" ") 
# ------------------------------------------------------------


# 2번 방법에서 dictionary 사용으로 시간복잡도 감소
import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))

compare = sorted(set(x)) # 중복 제거 및 정렬
dic = {compare[i] : i for i in range(len(compare))} # { dict[요소] : 요소의 index }


for i in x :
    print(dic[i], end=" ") # 인덱스가 좌표 압축 결과