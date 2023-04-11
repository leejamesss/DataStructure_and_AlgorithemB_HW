#插入节点X
def insertionUpdataBF(nd):           #插入过程修改nd的祖先BF
  if nd.BF ==2 or nd.BF==-2:         #nd失衡
    insertionRebalence(nd)           #调整
    return                           #调整完，结束
  if nd.father:                      #nd有父亲
    if nd.father.left is nd:
      nd.father.BF+=1
    else:
      nd.father.BF-=1
    if nd.father!=0:
      insertionUpdataBF(nd.father)

      
      
      
      
# 调整操作（V失衡后调整以V为根的子树）：
# 旋转操作：
# 1、LL旋转
  #新增的节点位于v的左子树的左子树
# 2、RR旋转
  #新增的节点位于V的右子树的右子树
  #BF=-2，BF=-1
# 3、LR旋转
  #新增的节点位于V的左子树的右子树
# 4、LR
  #新增的节点位于V的右子树的左子树
#注意之间的大小关系需要仍然满足二叉排序树

def insertionRebalence(self,nd):
  if nd.bf==2:
    if nd.left.bf==1:
      self.rotateLL(nd)
      

      
      
      
# Update   log(n)
# 旋转：O(1),是修改指针，旋转最多做一次

#堆和字典可以代替大部分AVL（平衡二叉树）的场景
#log(n)查找小于某个值的最大元素
#log(n)查找大于某个值的最小元素
#不破坏结构的情况下，O(n)从小到大遍历元素




