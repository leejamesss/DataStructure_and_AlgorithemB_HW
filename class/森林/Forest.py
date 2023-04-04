
#森林转二叉树
def woodToBinaryTree(woods):
  #woods是列表，每个元素都是一颗二叉树形式的树
  biTree=woods[0]                                 
  p=biTree                                         
  for i in range(1,len(woods)):                    
    p.addRight(woods[i])                           
    p=p.right
  return biTree
#biTree和woods共用节点，直接在原地更改


#二叉树转森林
def binaryTreeToWoods(tree):
  p=tree                                          #tree指的是二叉树
  q=p.right                                       #q是p的右节点
  p.right=None                                    
  woods=[p]
  if q:
    woods+=binaryTreeToWoods(q)
  return woods
#woods是兄弟-儿子树的列表，woods和tree共用节点，执行完后tree的元素不再是原本的儿子兄弟树
#就是没有复制节点，直接在原地更改
