# 정렬 문제
# p.359 Q-23 국영수

n = int(input())
score = [(name, int(kor), int(eng), int(math)) for name, kor, eng, math in 
         (input().split() for _ in range(n))]

sorted_score = sorted(score, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for x in sorted_score:
    print(x[0])