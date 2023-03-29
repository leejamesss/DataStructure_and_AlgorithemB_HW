# a[i][j]: number of ways to partition i into j positive integers
a = [[0 for _ in range(60)] for _ in range(60)]

def q1(N, k):
    for i in range(N+1):
        a[i][1] = 1
    
    for i in range(1, N+1):
        for j in range(2, k+1):
            a[i][j] = a[i-1][j-1]
            if i-j >= j:
                a[i][j] += a[i-j][j]

# b[i][j]: number of ways to partition N into distinct positive integers,
# where the largest number is at most T=N
b = [[0 for _ in range(60)] for _ in range(60)]

def q2(N, T):
    b[0][0] = 1
    for i in range(N+1):
        for t in range(1, T+1):
            b[i][t] = b[i][t-1]
            if i-t >= 0:
                b[i][t] += b[i-t][t-1]

# c[i][j]: number of ways to partition i into j odd positive integers
c = [[0 for _ in range(60)] for _ in range(60)]

def q3(N, t):
    for i in range(1, N+1, 2):
        c[i][1] = 1
    
    for i in range(2, N+1):
        for j in range(2, i+1):
            c[i][j] = c[i-1][j-1]
            if i-j >= j:
                c[i][j] += c[i-2*j][j]


while True:
    try:
        N, k = map(int, input().split())
        q1(N, k)
        print(a[N][k])
        
        q2(N, N)
        print(b[N][N])
        
        q3(N,N)
        sum = 0
        for i in range(1, N+1):
            sum += c[N][i]
        print(sum)
    except:
        break
