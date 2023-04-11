#深搜
def Dfs(V):
  #标记V为旧点
  #对和V相邻的每个点U;
  #DFS(U)
def main():
  #将所有点标记为新点
  #while(在图中能找到新点k)
  #Dfs(k)


  
#ps.邻接表和邻接矩阵，判断两个点之间的关系，邻接表的时间O(1),邻接矩阵的时间O(2n)/O(n)
  
  
  
#图的深度优先遍历--邻接表形式
def dfsTravel(G,op):
  def dfs(v):
    visited[v]=True
    op(v)
    for u in G[v]:
      if not visited[u]:
        dfs(u)
  n=len(G)
  visited=[False for i in range(n)]
  for i in range(n):
    if not visited[i]:
      dfs(i)
      
#每个顶点看过一遍，每条边看过一遍(无向图两遍) ，复杂度O(E+V),E是边数,V是顶点数 
  
