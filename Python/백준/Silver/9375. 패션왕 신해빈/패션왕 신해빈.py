# 서로 다른 종류의 옷이 여러 개 있을 때, 
# 각 종류에서 0개 또는 1개를 선택하는 모든 경우의 수 계산
# 단, 아무것도 안 입는 경우는 제외

# 옷 종류 a, b, c, d 4종류
# 각각 1, 2, 3, 4개의 옷이 있다면
# - 각 종류에서 입을 옷 선택: 1C1 = 1, 2C1 = 2, 3C1 = 3, 4C1 = 4
# - 각 종류를 입을지 말지 결정: 2 (입음/안 입음)
# 따라서 전체 경우 수: (1*2) * (2*2) * (3*2) * (4*2) - 1

t = int(input())  

for _ in range(t):
    n = int(input()) 

    # {'headgear': 2, 'eyewear': 1} 딕셔너리 생성
    clothes = {}     
    
    for _ in range(n): 
        name, type = input().split()  
        if type not in clothes:
            clothes[type] = 1      # 새로운 종류면 1로 초기화
        else:
            clothes[type] += 1     # 이미 있는 종류면 개수 +1

    result = 1
    # 각 종류마다 (해당 종류 옷 개수 + 1)을 곱함
    # +1은 안 입는 경우 포함
    for count in clothes.values():
        result *= (count + 1)  

    result -= 1  # 아무것도 안 입는 경우 제외
    print(result)  
