import math
# 브루트포스
n = int(input())

def is_square(num):
    if math.sqrt(num)==int(math.sqrt(num)):
        return True
    else:
        return False

_min=4
if is_square(n): # 1. n이 제곱수인 경우
    _min=1
else:
    for i in range(int(math.sqrt(n)),0,-1):
        # 2. 두 제곱수의 합인 경우(=2) / 제곱수를 뺀 값이 제곱수인 경우
        if is_square(n-(i**2)):
            _min=2
            break
        else: # 3. 세 제곱수의 합인 경우(=3)
            for j in range(int(math.sqrt(n-i**2)),0,-1):
                if is_square(n-(i**2)-(j**2)):
                    _min=3
                    break

print(_min)