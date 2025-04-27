# 구현 문제
# p.327 Q-11 뱀

n = int(input())
k = int(input())

apple = []
for i in range(k) :
    row, col = map(int, input().split())
    apple.append([row-1, col-1])
    
l = int(input())
sec = []
turn = []

for i in range(l) :
    x, c = input().split()
    sec.append(x)
    turn.append(c)
    
s_row = 0
s_col = 0
dir = 'r'
s_body = [[0, 0]]
time = 0
turn_count = 0


while True: 
    time += 1
        
    if dir == 'r' :
        s_col += 1
            
    elif dir == 'd' :
        s_row += 1
                
    elif dir == 'l' :
        s_col -= 1
    else :
        s_row -= 1
        
    
    if (s_row < 0 or s_row > n-1 or s_col < 0 or s_col > n-1) or ([s_row, s_col] in s_body) :
        break
        
    s_body.append([s_row, s_col])
        
    if [s_row, s_col] in apple :
        apple.remove([s_row, s_col])
    else: 
        s_body.pop(0)
        
    
    if turn_count < l and time == int(sec[turn_count]):
        if turn[turn_count] == 'D':
            if dir == 'r':
                dir = 'd'
            elif dir == 'd':
                dir = 'l'
            elif dir == 'l':
                dir = 'u'
            else:
                dir = 'r'
        else:
            if dir == 'r':
                dir = 'u'
            elif dir == 'u':
                dir = 'l'
            elif dir == 'l':
                dir = 'd'
            else:
                dir = 'u'
        
        turn_count += 1

    
print(time)