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
# 3、LR
  #新增的节点位于V的
# 4、LR
