s=list(input())
s.sort()
N=len(s)
result=[0 for i in range(N)]
used=[False for i in range(N)]
def dfs(n):
    if n==N:
        print(''.join(result))
    for i in range(N):
        if not used[i]:
            result[n]=s[i]
            used[i]=True
            dfs(n+1)
            used[i]=False
dfs(0)
