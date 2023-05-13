n=int(input())
graph=[]
for i in range(n-1):
    op=input().split()
    for j in range(int(op[1])):
        #op[0]和[2]，[4],...,[2n]
        graph.append([op[0],op[2*j+2],op[2*j+3]])
adj=[]

#构建邻接矩阵的行,每行代表一个顶点
for i in range(n):
    adj.append([])
    #构建邻接矩阵的列
    for j in range(n):
        adj[i].append(0)

#构建邻接矩阵的值
for i in range(len(graph)):
    adj[ord(graph[i][0])-ord('A')][ord(graph[i][1])-ord('A')]=int(graph[i][2])
    adj[ord(graph[i][1])-ord('A')][ord(graph[i][0])-ord('A')]=int(graph[i][2])


#定义顶点个数
V=n
#定义顶点列表
nodes=[]
for i in range(V):
    nodes.append(chr(ord('A')+i))

# 定义一个字典，用来存储邻接矩阵的二维数组形式
adj_matrix = {}

# 遍历每个顶点，初始化字典的值为一个长度为V的零列表
for node in nodes:
    adj_matrix[node] = [0] * V
# 遍历邻接矩阵列表，根据顶点的索引，更新字典的值为对应的权值
for u,v,w in graph:
    i = nodes.index(u)
    j = nodes.index(v)
    adj_matrix[u][j] = int(w)
    adj_matrix[v][i] = int(w)

INF=999999999

# 定义一个数组记录选择的顶点
selected = [False] * V
# 设置边的数量为零
no_edge = 0
# 把第一个顶点设为已选择
selected[nodes.index("A")] = True

sum=0
while (no_edge < V - 1):
    # 对于每个已选择的顶点，找到所有相邻的未选择的顶点，计算它们之间的距离
    # 如果距离小于当前的最小值，就更新最小值和对应的顶点
    minimum = INF
    x = -1
    y = -1
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if (not selected[j]) and adj_matrix[nodes[i]][j]:
                    if minimum > adj_matrix[nodes[i]][j]:
                        minimum = adj_matrix[nodes[i]][j]
                        x = i
                        y = j

    sum+=adj_matrix[nodes[x]][y]
    selected[y] = True
    no_edge +=1
print(sum)
