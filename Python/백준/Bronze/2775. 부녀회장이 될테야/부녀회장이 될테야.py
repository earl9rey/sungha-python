t = int(input())

for _ in range(t) :
    k = int(input())
    n = int(input())

    resident = []
    for i in range(k+1):
        row = []
        for j in range(n+1):
            row.append(0) 
        resident.append(row) 
            
    for i in range(k+1) :
        for j in range(n+1) :
            if i == 0 :
                resident[i][j] = j
            else :
                for m in range(j+1) :
                    resident[i][j] += resident[i-1][m]
    
    print(resident[k][n])