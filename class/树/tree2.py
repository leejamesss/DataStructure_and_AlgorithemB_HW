
#儿子兄弟表示法（利用二叉树表示树）（把原本的兄弟变为父子）
#没有右节点
#使用范围：没有可变长的数列的时候


#树的直观表示法转儿子兄弟树
def treeToBinaryTree(tree):
  bTree=Binary(tree.data)                                 #两个的树根是一样的                  
  for i in range(len(tree.subtrees)):                     
    if i ==0:
      tmpTree=treeToBinaryTree(tree.subtrees[i])                    #长子节点转换为树
      bTree.addLeft(tmpTree)                                        #添加到左边（比较年长）
    else:                                                 
      tmpTree.addRight(treeToBinaryTree(tree.subtrees[i]))          #如果见到了其他儿子，加到右边，因为辈分排在后
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


#树的前序遍历序列和儿子兄弟树的前序遍历序列一致
#树的后序遍历序列和儿子兄弟树的中序遍历序列一致

#儿子兄弟树中，对应到树中，左手是儿子，右手是兄弟

