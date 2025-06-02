# DFS/BFS
# p.349 Q-19 연산자 끼워 넣기

from itertools import permutations

n = int(input())
num = list(map(int, input().split()))

plus, minus, mul, div = map(int, input().split())
ops = ['+'] * plus + ['-'] * minus + ['*'] * mul + ['/'] * div # 연산자별 입력 개수만큼 문자열 생성
operation = set(permutations(ops, len(ops))) # 순서와 중복을 고려하여 순열 찾기

results = []

for op in operation : # 모든 순열에 대해
    result = num[0]
    for i in range(n-1) : # 입력 받은 피연산자(숫자)들을 순차적으로 계산
        if op[i] == "+" :
            result += num[i+1]
        elif op[i] == "-" :
            result -= num[i+1]
        elif op[i] == "*" :
            result *= num[i+1]
        else :
            if result < 0:
                result = -(-result // num[i + 1])
            else:
                result = result // num[i + 1]
    results.append(result) # 각 순열에 대한 계산 결과값 리스트에 저장

print(max(results))
print(min(results))