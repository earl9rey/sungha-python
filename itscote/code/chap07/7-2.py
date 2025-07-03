# 이진 탐색 
# p.197 실전 문제 7-2 부품 찾기

n = int(input())
nlist = list(map(int, input().split()))
m = int(input())
mlist = list(map(int, input().split()))

def search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) //2

    if array[mid] == target :
        return mid
    elif array[mid] > target :
        return search(array, target, start, mid-1)
    else:
        return search(array, target, mid+1, end)
     
for target in mlist :
    result = search(nlist, target, 0, n-1)
    if result == None:
        print("No", end=" ")
    else:
        print("Yes", end=" ")