# 정렬
# p.178 실전 문제 6-2 위에서 아래로

n = int(input())
sequence = [int(input()) for _ in range(n)]

def selection(array) :
    for i in range(len(array)):
        min_index = i # 가장 작은 원소의 인덱스
        for j in range( i + 1, len(array)):
            if array[min_index] < array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

    return array

def insertion(array) :
    for i in range(1, len(array)):
        for j in range(i, 0, -1): # 인덱스 i부터 1 까지 감소하며 반복하는 문법
            if array[j ] > array[j - 1]: # 한 칸씩 왼쪽으로 이동
                array[j], array[j - 1] = array[j - 1], array[j]
            else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
                break
    return array

def quick(array):
# 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1 :
        return array   
    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트
    
    left = [x for x in tail if x >= pivot] # 분할된 왼쪽 부분
    right = [x for x in tail if x < pivot] # 분할된 오른쪽 부분
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick(left) + [pivot] + quick(right)

print("선택 정렬: ", selection(sequence))
print("삽입 정렬: ", insertion(sequence))
print("퀵 정렬: ", quick(sequence))