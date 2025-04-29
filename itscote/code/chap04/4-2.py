# 구현
# p.115 실전 문제 4-2 왕실의 나이트

knight = input()

list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
row = list.index(knight[0]) + 1
col = int(knight[1])

move = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
count = 0

for i in move: 
    r = row + i[0]
    c = row + i[1]
    if ( 1 <= r <= 8 and 1 <= c <= 8 ) :
        count += 1

print(count)