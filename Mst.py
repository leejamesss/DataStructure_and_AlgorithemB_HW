# def dfsMst(G):
#     n=len(G)
#     father =[-1 for i in range(n)]
#     def dfs(v,f):
#         father[v] =f
#         for u in G[v]:
#             if father[u] ==-1:
#                 dfs(u,v)
#     dfs(0,0)
#     result =[]
#     for i in range(n):
#         if father[i]!=i:
#             result.append((father[i],i))
#     return result
