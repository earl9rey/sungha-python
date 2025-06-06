# 정렬
# p.180 실전 문제 6-3 성적이 낮은 순서로 학생 출력하기

n = int(input())
grade = [] # dictionary 자료구조 사용

for _ in range(n):
    name, score = input().split()
    grade.append([name, int(score)]) 

def selection(array) :
    for i in range(len(array)):
        min_index = i 
        for j in range( i + 1, len(array)):
            if array[min_index][1] > array[j][1]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

    return array


for i in range(n) :
    print(selection(grade)[i][0], end=' ')