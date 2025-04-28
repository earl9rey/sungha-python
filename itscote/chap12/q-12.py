# 구현 문제
# p.329 Q-12 기둥과 보 설치

def solution(n, build_frame):
    structure = []  # 현재 설치된 기둥과 보를 저장하는 배열

    # 전체 작업 처리
    for x, y, a, b in build_frame:
        if b == 1:  # 설치하는 경우
            structure.append([x, y, a])  # 일단 설치
            if check(structure) == False:  # 설치 후 전체 구조 확인
                structure.remove([x, y, a])  # 안 되면 다시 제거
        else:  # 삭제하는 경우
            structure.remove([x, y, a])  # 일단 삭제
            if check(structure) == False:  # 삭제 후 전체 구조 확인
                structure.append([x, y, a])  # 안 되면 다시 복구

    # 결과를 정렬해서 리턴해야 함 (문제 조건)
    structure.sort(key=lambda x: (x[0], x[1], x[2]))
    return structure


# 구조가 정상인지 검사하는 함수
def check(structure):
    for x, y, a in structure:
        if a == 0:  # 기둥인 경우
            # 바닥 위이거나, 아래에 기둥이 있거나, 보의 한쪽 끝 위에 있으면 ok
            if y == 0 or [x, y-1, 0] in structure or [x-1, y, 1] in structure or [x, y, 1] in structure:
                continue
            return False  # 조건 안 맞으면 False
        else:  # 보인 경우
            # 아래에 기둥이 있거나, 양쪽에 보가 있으면 ok
            if ([x, y-1, 0] in structure) or ([x+1, y-1, 0] in structure) or ([x-1, y, 1] in structure and [x+1, y, 1] in structure):
                continue
            return False  # 조건 안 맞으면 False
    return True  # 모두 조건을 만족하면 True
