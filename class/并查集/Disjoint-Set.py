
#并查集
#概念：N个元素，分布在一些不相交的集合
#实质：树
#操作：
#1、合并a、b两个元素所在的集合Merge(a,b)      
#2、查询元素在哪个集合
#3、查询两个元素是否在一个集合Query(a,b)     

#简单算法-集合编号，元素编号
# 合并：O(n)
# 查询：O(1)




#用树表示集合的算法
#实质：用parent标记集合
#操作：
  #Query(a,b)
  #-比较b和a所在的树根节点是否相同
  #Merge(a,b)
  #-将b的树根的父亲设置为a的树根
  #缺点：
  #寻找树根的时间复杂度：没有控制树的深度
  

#parent规则：
#没有parent的自己就是parent


#基本操作：GetRoot(a):求树根
def GetRoot(a):
  if parent[a]==a：
    return a
  return GetRoot(parent[a])       #顺藤摸瓜

# 优化方法：
#1、矮的挂在高的根节点下面
#2、路径压缩
def GetRoot(a):
  if parent[a]!=a:
    parent[a]=GetRoot(parent[a])
  return parent[a]
parent =[i for i in range(N)]
def Merge(a,b):
  #b挂在a树根下
  parent[GetRoot(b)]=GetRoot(a)
def Query(a,b):
  #查询a，b是否位于同一棵树
  return GetRoot(a)==GetRoot(b)


#查询一次后就改造树,全部改造成直系亲属，树的深度<=2




