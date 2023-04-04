#元素的添加、删除、查找
#二叉查找树：中序遍历序列是递增序列<=>二叉树是二叉搜索树


#二叉排序树查找



#二叉排序树插入（递归插入）

#删除
#1、叶子：直接删除
#2、只有1子节点：左/右边的来替换位置
#3、有两个子节点：


class  BinarySearchTree:
  class Node:
    def __init__(self,key,data,left=None,right=None):
      self.key,self.value,self.left,self.right=key,data,left,right
  def __init__(self,less=lambda x,y:x<y):
    self.root,self.size=None,0
    self.less=less
  def _find(self,key):
    def find(root,father):
      if self.less(key,root.key):
        if root.left:
          return find(root.left,root)
        else:
          return None,None 
      elif self.less(root.key,key):
        if root.right:
          return find(root.right,root)
        else:
          return None,None 
      else:
        return root,father
    if self.root is None:
      return None,None
    return find(self.root,None)
  def _insert(self,key,data):
    def insert(root):
      if self.less(key,root.key):
        if root.left is None:
          root.left =BinarySearchTree.Node(key,data)
          return True
        else:
          return insert(root.left）
      elif self.less(root.key,key):
        if 
          
          
          
