
#儿子兄弟表示法（利用二叉树表示树）（把原本的兄弟变为父子）
#没有右节点
#使用范围：没有可变长的数列的时候


#树的直观表示法转儿子兄弟树
def treeToBinaryTree(tree):
  bTree=Binary(tree,data)
  for i in range(len(tree.subtrees)):
    if i ==0:
      tmpTree=treeToBinaryTree(tree.subtrees[i])
      bTree.addLeft(tmpTree)
    else:
      tmpTree.addRight(treeToBinaryTree(tree.subtrees[i]))
      tmpTree= tmpTree.right
  return btree


#树的儿子兄弟树表示法转换为直观表示法

def binaryTreeToTree(biTree):
  tree=Tree(biTree.data)
  son=biTree.left
  if son:
    tree.addSubTree(binaryTreeToTree(son))
    while son.right:
      tree.addSubTree(binaryTreeToTree(son.right))
      son=son.right
  return tree


#实质：树的左边比较优先，能够成为老大，在儿子兄弟表示法中可以成为父亲
