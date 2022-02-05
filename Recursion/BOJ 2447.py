N = int(input())
array = [[' ' for i in range(N)] for j in range(N)]

def recur(x, y, N) :
    if N == 3 : 
        for i in range(3) :
            for j in range(3) :
                if i == 1 and j == 1 :
                    pass
                else : 
                    array[x+i][y+j] = '*'
    
    else : 
        size = int(N / 3)
        for i in range(3) :
            for j in range(3) :
                if i == 1 and j == 1:
                    pass
                else :
                    recur(x + i * size, y + j * size, size)
       
recur(0, 0, N)
                    
for i in range(N):
    for j in range(N):
        print(array[i][j], end='')
    print()

