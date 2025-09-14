# 잃어버린 괄호 (구글링 - 그리디)

#   예: "50-40+30-20+10"
#   → split('-') = ["50", "40+30", "20+10"]
#   → 첫 그룹(50)은 더하고, 이후 그룹(40+30), (20+10)은 전부 뺌


exp = input()

# '-' 기준으로 나누기
#   → 첫 번째 그룹은 그냥 더하고,
#   → 그 이후 그룹은 모두 빼야 최소값을 만들 수 있음
sub = exp.split('-')

# 첫 번째 그룹(맨 앞)은 '+' 기준으로 다시 나눠서 전부 더하기
add = sub[0].split('+')
res = 0
for i in add:
    res += int(i)

# 두 번째 그룹부터는 모두 빼기
for i in range(1, len(sub)):
    tmp = sub[i].split('+')   # '+' 있으면 다 분리
    for ele in tmp:
        res -= int(ele)       # 전부 빼기

print(res)
