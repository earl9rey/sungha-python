# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

# 입력: 첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)
# 출력: 첫째 줄에 구한 0의 개수를 출력한다.

n = int(input())

# n! 계산 
factorial = 1
for i in range(n) :
    factorial *= i+1 

# n! 문자열 리스트로 바꾼 후 순서 뒤집기
nums = str(factorial)
rev = nums[::-1]

# 처음 0이 아닌 숫자가 나오는 인덱스 출력 (= 0 개수)
for j in range(len(rev)) :
    if rev[j] != '0' :
        print(j)
        break
