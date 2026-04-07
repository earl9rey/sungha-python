# 11053 가장 긴 증가하는 부분 수열

n = int(input())                     
a = list(map(int, input().split())) 

# result[i] = i번째 숫자를 마지막으로 했을 때 만들 수 있는 가장 긴 증가하는 수열의 길이
result = [1] * n

# i번째 숫자를 기준으로,앞에 있는 숫자들(j)을 모두 비교
for i in range(1, n):
    for j in range(i):

        # 만약 앞의 숫자 a[j]가 현재 숫자 a[i]보다 작으면 증가하는 형태가 가능하다는 뜻
        if a[i] > a[j]:

            # j에서 끝나는 증가 수열 뒤에 a[i]를 붙일 수 있으므로, 그 길이(result[j] + 1)와 지금까지의 값 중 더 큰 값 저장
            result[i] = max(result[i], result[j] + 1)

# result 리스트 중 가장 큰 값이 곧 전체에서 만들 수 있는 가장 긴 증가하는 부분 수열의 길이
print(max(result))
