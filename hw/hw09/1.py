n,m=map(int,input().split())
#表示无向图有n个顶点，m条边
#构建邻接表
adj=[[] for i in range(n)]
for i in range(m):
    #读入m条边,#表示一条边连接u和v
    u,v=map(int,input().split())
    #构建邻接表,邻接表的第i个元素是一个列表，表示顶点i的邻接点
    adj[u].append(v)
    adj[v].append(u)


#深度优先遍历
def dfsTravel(adj,op):
    #adj是邻接表，op是对顶点进行的操作
    #visited[i]表示顶点i是否被访问过
    visited=[False for i in range(len(adj))]
    def dfs(v):
        #访问顶点v
        visited[v]=True
        #对顶点v进行操作
        op(v)
        #遍历顶点v的邻接点
        for each in adj[v]:
            if not visited[each]:
                dfs(each)
    n=len(adj)
    for i in range(n):
        if not visited[i]:
            dfs(i)


dfsTravel(adj,lambda x:print(x,end=' '))
