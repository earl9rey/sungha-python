# M 이상 N 이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# [입력] 
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) 
# M 이상 N 이하의 소수가 하나 이상 있는 입력만 주어진다.

# [출력]
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

## 구글링 

m, n = map(int, input().split())

for i in range(m, n+1):
    if i == 1: # 1은 통과
        continue
        
    for j in range(2, int(i**0.5) + 1): # 2 ~ 제곱근 사이 값 확인
        if i % j == 0: # 나누어 떨어진다면 그대로 종료 (else문 실행 X)
            break
    else: # for문이 잘 실행이 되었다면 print(i) 출력
        print(i)
