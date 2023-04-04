# # 有n个学生，编号0到 n-1, 以及m个团体， (0 < n <=
# 30000 , 0 <= m <= 500) 一个学生可以属于多个团体
# ，也可以不属于任何团体。一个学生得病，则它所
# 属的整个团体都会被他传染而得病。
# 
# 开始只有0号学生得病。已知每个团体都由哪些学生
# 构成， 求最终一共多少个学生会得病。

MAX=30000
parent=[0 for i in range(MAX+10)]
total=[0 for i in range(MAX+10)]                        #total记录的是以i为树根的得病集合的人数
#total[GetRoot(a)]是a 所在的group的人数
def GetRoot(a):
  if parent[a]!=a:
    parent[a]=GetRoot(parent[a])
  return parent[a]

def Merge(a,b):
  p1=GetRoot(a)
  p2=GetRoot(b)
  if p1=p2:
    return
  total[p1]+=total[p2]                                  #维护了total
  parent[p2]=p1                                         #p2合并到p1下面

  
while True:
  n,m=list(map(int,input().split()))
  if n==0 and m==0:
    break
  for i in range(n):
    parent[i]=i
    total[i]=1                                          #每个人自成一个集合
  for i in range(m):
    lst=list(map(int,input.split()))
    k=lst[0]
    h=lst[1]
    for j in range(2,k+1):
      Merge(h,lst[j])
    print(total[GetRoot(0)])                            #total(0)和parent(0)[需要路径压缩后]不行，因为不一定是树根
    
