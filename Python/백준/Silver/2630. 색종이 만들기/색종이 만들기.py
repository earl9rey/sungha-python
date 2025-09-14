# 색종이 만들기 (분할 정복, 재귀 사용)

# 틀림 (이유 모르겠음 ㅠㅠ) -----------------------------------------------------------------------
    
    # # 재귀 함수 : n x n 크기의 종이를 받아 색종이 개수를 세는 함수
    # def cut(n, paper) :
    #     # 종이 크기가 1x1일 때
    #     if n == 1:
    #         if paper[0][0] == 0:    # 색이 0이면 흰색
    #             return 1, 0          # 흰색 1장, 파란색 0장
    #         else:                   # 색이 1이면 파란색
    #             return 0, 1          # 흰색 0장, 파란색 1장
        
    #     half = n // 2
    #     count0, count1 = 0, 0      

    #     # 4분면으로 종이 나누기
    #     p1 = [row[0:half] for row in paper[:half]]      # 왼쪽 위
    #     p2 = [row[half:n] for row in paper[:half]]      # 오른쪽 위
    #     p3 = [row[0:half] for row in paper[half:]]      # 왼쪽 아래
    #     p4 = [row[half:n] for row in paper[half:]]      # 오른쪽 아래
        
    #     # 각 사분면에 대해 색이 모두 같으면 바로 카운트, 아니면 재귀
    #     for p in [p1, p2, p3, p4]:
    #         if all(x == 0 for row in p for x in row):    # 사분면이 모두 0이면
    #             count0 += 1                              # 흰색 1장 추가
    #         elif all(x == 1 for row in p for x in row):  # 사분면이 모두 1이면
    #             count1 += 1                              # 파란색 1장 추가
    #         else :                                        # 혼합된 경우
    #             c0, c1 = cut(n//2, p)                   # 재귀 호출
    #             count0 += c0                             # 재귀에서 나온 흰색 합산
    #             count1 += c1                             # 재귀에서 나온 파란색 합산
        
    #     return count0, count1


    # n = int(input())             
    # paper = []                    

    # for i in range(n) :
    #     lst = list(map(int, input().split())) 
    #     paper.append(lst)                    

    # white, blue = cut(n, paper)

    # print(white)  
    # print(blue)   

# ------------------------------------------------------------------------------------

# 색종이 분할 재귀 함수 정의 
    # a, b : 현재 종이의 왼쪽 위 좌표
    # n    : 현재 종이의 한 변 길이
def paper(a, b, n):
    global white, blue
    
    color = field[a][b]  # 현재 종이의 기준 색상 (왼쪽 위 색상)
    
    # 현재 n x n 종이 내부를 검사
    for i in range(a, a+n):
        for j in range(b, b+n):
            if color != field[i][j]:  # 한 칸이라도 기준 색과 다르면
                # 종이를 4등분하여 재귀 호출
                paper(a, b, n//2)                 # 왼쪽 위
                paper(a + n//2, b, n//2)          # 왼쪽 아래
                paper(a, b + n//2, n//2)          # 오른쪽 위
                paper(a + n//2, b + n//2, n//2)   # 오른쪽 아래
                return                            # 더 이상 검사하지 않고 재귀로 넘어감
    
    # 모든 칸이 동일 색이면 해당 색 카운트 증가
    if color == 0:
        white += 1   # 흰색 색종이
    else:
        blue += 1    # 파란색 색종이

global white, blue
white, blue = 0, 0

n = int(input()) 
field = [list(map(int,input().split())) for _ in range(n)]  # 종이 정보 입력

paper(0, 0, n)

print(white) 
print(blue)   
