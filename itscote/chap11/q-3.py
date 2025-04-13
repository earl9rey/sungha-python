# 그리디 문제
# p.313 Q-03 문자열 뒤집기

# 문자열 데이터 입력
s = input()

# 변수 초기화 
count = 0 # 값이 달라지는 횟수
num = s[0] # 데이터의 각 원소

# 모든 문자열 배열 원소를 순회하면서 값이 달라지는 횟수 (count) 찾기
for i in s:
    if num == i :
        num = i
        continue
    else :
        count += 1
        num = i
        continue
    
# 뒤집기 최소 횟수 (result) 계산
result = (count + 1) // 2

print(result)