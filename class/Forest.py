
#森林转二叉树
def woodToBinaryTree(woods):
  biTree=woods[0]                                  #森林的根就是第一棵树的根
  p=biTree                                         #指针，初始位置为森林的根
  for i in range(1,len(woods)):                    
    p.addRight(woods[i])                           #指针增加这个
    p=p.right
  return biTree

#二叉树转森林
def binaryTreeToWoods(tree):
  p=tree
  q=p.right
  p.right=None
  woods=[p]
  if q:
    woods+=binaryTreeToWoods(q)
  return woods
