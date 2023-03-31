# a[i][j]: number of ways to partition i into j positive integers
a = [[0 for _ in range(60)] for _ in range(60)]

def q1(N, k):                                   #N表示要划分的整数，k表示划分的个数
    for i in range(N+1):
        a[i][1] = 1                             #初始化
    
    for i in range(1, N+1):                     
        for j in range(2, k+1):
            a[i][j] = a[i-1][j-1]               #第一个正整数为1时的情况
            if i-j >= j:                        #第一个正整数大于1的情况
                a[i][j] += a[i-j][j]            #相加

# b[i][j]: number of ways to partition N into distinct positive integers,
# where the largest number is at most T=N
b = [[0 for _ in range(60)] for _ in range(60)]

def q2(N, T):
    b[0][0] = 1                                 #引入参数T，表示划分数中的最大值
    for i in range(N+1):                        #遍历数组进行填充
        for t in range(1, T+1):                 
            b[i][t] = b[i][t-1]                 #分解的数字中不包含t的情况
            if i-t >= 0:                        
                b[i][t] += b[i-t][t-1]          #分解的数字中包含t的情况

# c[i][j]: number of ways to partition i into j odd positive integers
c = [[0 for _ in range(60)] for _ in range(60)]

def q3(N, t):                                   #N是要分割的数字，t是分割的数字中的最大值
    for i in range(1, N+1, 2):                  
        c[i][1] = 1                             #初始化，t=1的时候就是1
    
    for i in range(2, N+1):                     #i分为两部分，一个是1个奇数（1-t），一个是其余的j-1个奇数（和为i-第一个奇数）
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
